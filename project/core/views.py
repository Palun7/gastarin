from django.shortcuts import render, redirect
from gastos.models import Gasto, Gasto_fijo, Ingreso, Cuota
from django.db.models import Sum
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Count, F, Q, OuterRef, Subquery, Prefetch
from .models import Recomendaciones
from datetime import date
from django.utils.dateparse import parse_date

def transformar_mes(numero):
    meses = {
        1: 'Enero', 2: 'Febrero', 3: 'Marzo',
        4: 'Abril', 5: 'Mayo', 6: 'Junio',
        7: 'Julio', 8: 'Agosto', 9: 'Septiembre',
        10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
    }
    return meses.get(numero)


@login_required(login_url='usuarios:login-registro')
def index(request):
    if request.method == 'POST' and 'cuota_id' in request.POST:
        cuota_id = request.POST.get('cuota_id')

        cuota = Cuota.objects.get(
            id=cuota_id,
            gasto__usuario=request.user
        )

        if not cuota.pagada:
            cuota.pagada = True
            cuota.fecha_pago = timezone.now().date()
            cuota.save()

        return redirect('core:index')

    hoy = timezone.now()
    filtro_tipo = request.GET.get('filtro', 'mes')

    desde = parse_date(request.GET.get('desde') or '')
    hasta = parse_date(request.GET.get('hasta') or '')

    filtros = {
        'usuario': request.user,
    }

    if filtro_tipo == 'personalizado' and desde and hasta:
        filtros['fecha__range'] = (desde, hasta)
        titulo = f"Del {desde.strftime('%d/%m/%Y')} al {hasta.strftime('%d/%m/%Y')}"

    elif filtro_tipo == 'dia':
        filtros['fecha__year'] = hoy.year
        filtros['fecha__month'] = hoy.month
        filtros['fecha__day'] = hoy.day
        titulo = "Hoy"

    elif filtro_tipo == 'mes':
        filtros['fecha__year'] = hoy.year
        filtros['fecha__month'] = hoy.month
        titulo = transformar_mes(hoy.month)

    elif filtro_tipo == 'anio':
        filtros['fecha__year'] = hoy.year
        titulo = f"{hoy.year}"

    elif filtro_tipo == 'historico':
        titulo = "Histórico"

    else:
        filtros['fecha__year'] = hoy.year
        filtros['fecha__month'] = hoy.month
        titulo = transformar_mes(hoy.month)

    # =========================
    # INGRESOS
    # =========================

    ingreso_total = Ingreso.objects.filter(
        **filtros
    ).aggregate(
        total=Sum('monto')
    )['total'] or 0

    # =========================
    # CUOTAS PAGADAS
    # =========================

    filtros_cuotas = {
        'gasto__usuario': request.user,
        'pagada': True
    }

    if filtro_tipo == 'personalizado' and desde and hasta:
        filtros_cuotas['fecha_pago__range'] = (desde, hasta)

    elif filtro_tipo == 'dia':
        filtros_cuotas['fecha_pago__year'] = hoy.year
        filtros_cuotas['fecha_pago__month'] = hoy.month
        filtros_cuotas['fecha_pago__day'] = hoy.day

    elif filtro_tipo == 'mes':
        filtros_cuotas['fecha_pago__year'] = hoy.year
        filtros_cuotas['fecha_pago__month'] = hoy.month

    elif filtro_tipo == 'anio':
        filtros_cuotas['fecha_pago__year'] = hoy.year

    gasto_cuotas = Cuota.objects.filter(
        **filtros_cuotas
    ).aggregate(
        total=Sum('monto')
    )['total'] or 0

    # =========================
    # GASTOS DIARIOS
    # =========================

    gasto_diario = Gasto.objects.filter(
        **filtros
    ).aggregate(
        total=Sum('monto')
    )['total'] or 0

    # =========================
    # GASTOS FIJOS SIN CUOTAS
    # =========================

    gasto_fijo = Gasto_fijo.objects.filter(
        **filtros
    ).filter(
        Q(cuotas__isnull=True) | Q(cuotas=0)
    ).aggregate(
        total=Sum('monto')
    )['total'] or 0

    # =========================
    # TOTALES
    # =========================

    gasto_total = gasto_diario + gasto_cuotas + gasto_fijo

    saldo = ingreso_total - gasto_total

    saldo_rojo = saldo if saldo < 0 else None

    # =========================
    # LISTA DE CUOTAS ACTIVAS
    # =========================

    ultima_cuota = Cuota.objects.filter(
        gasto=OuterRef('pk'),
        pagada=True
    ).order_by('-fecha_pago', '-numero')

    lista_cuotas = Gasto_fijo.objects.filter(
        usuario=request.user,
        cuotas__isnull=False
    ).exclude(
        cuotas=0
    ).annotate(
        total_cuotas=Count('cuota'),
        cuotas_pagadas=Count('cuota', filter=Q(cuota__pagada=True)),
        ultima_cuota_pagada_numero=Subquery(ultima_cuota.values('numero')[:1]),
        ultima_cuota_pagada_fecha=Subquery(ultima_cuota.values('fecha_pago')[:1]),
    ).exclude(
        total_cuotas=F('cuotas_pagadas')
    ).prefetch_related(
        Prefetch('cuota_set', queryset=Cuota.objects.order_by('numero'))
    )

    cantidad = len(lista_cuotas)

    # =========================
    # ÚLTIMOS MOVIMIENTOS
    # =========================

    lista_gastos_diarios = Gasto.objects.filter(
        **filtros
    ).order_by('-fecha')[:5]

    lista_gastos_fijos = Gasto_fijo.objects.filter(
        **filtros
    ).filter(
        cuotas__isnull=True
    ).order_by('-fecha')[:5]

    lista_ingresos = Ingreso.objects.filter(
        **filtros
    ).order_by('-fecha')[:5]

    cuotas_pagadas = Cuota.objects.filter(**filtros_cuotas).order_by('-fecha_pago')[:5]

    return render(request, 'core/index.html', {
        'ingreso': ingreso_total,
        'gasto_total': gasto_total,
        'saldo': saldo,
        'saldo_rojo': saldo_rojo,
        'titulo': titulo,
        'filtro_activo': filtro_tipo,
        'desde': desde,
        'hasta': hasta,
        'lista_cuotas': lista_cuotas,
        'cantidad': cantidad,
        'lista_gastos_diarios': lista_gastos_diarios,
        'lista_gastos_fijos': lista_gastos_fijos,
        'lista_ingresos': lista_ingresos,
        'cuotas_pagadas': cuotas_pagadas,
    })

@require_POST
def toggle_cuota(request, cuota_id):
    cuota = Cuota.objects.get(id=cuota_id)
    cuota.pagada = not cuota.pagada
    cuota.save()

    return JsonResponse({'ok': True})

def recomendaciones(request):
    user = request.user

    recomendaciones = Recomendaciones.objects.filter(usuario=user)

    recomendaciones_admin = Recomendaciones.objects.all()

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        texto = request.POST.get('texto')
        foto = request.FILES.get('foto')

        Recomendaciones.objects.create(
            usuario=user,
            titulo=titulo,
            texto=texto,
            foto=foto,
        )
        return redirect('core:recomendaciones')



    return render(request, 'core/recomendaciones.html', {
        'recomendaciones':recomendaciones,
        'recomendaciones_admin': recomendaciones_admin,
    })