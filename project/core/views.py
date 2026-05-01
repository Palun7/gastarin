from django.shortcuts import render
from gastos.models import Gasto, Gasto_fijo, Ingreso, Cuota
from django.db.models import Sum
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Count, Q, F


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
    hoy = timezone.now()

    filtro_tipo = request.GET.get('filtro', 'mes')

    filtros = {
        'usuario': request.user,
    }

    if filtro_tipo == 'dia':
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

    # ✅ INGRESOS
    ingreso_total = Ingreso.objects.filter(**filtros)\
        .aggregate(total=Sum('monto'))['total'] or 0

    # ✅ FILTROS PARA CUOTAS (ACÁ ESTÁ EL CAMBIO)
    filtros_cuotas = {
        'gasto__usuario': request.user,
        'pagada': True
    }

    if filtro_tipo == 'dia':
        filtros_cuotas['gasto__fecha__year'] = hoy.year
        filtros_cuotas['gasto__fecha__month'] = hoy.month
        filtros_cuotas['gasto__fecha__day'] = hoy.day

    elif filtro_tipo == 'mes':
        filtros_cuotas['gasto__fecha__year'] = hoy.year
        filtros_cuotas['gasto__fecha__month'] = hoy.month

    elif filtro_tipo == 'anio':
        filtros_cuotas['gasto__fecha__year'] = hoy.year

    # histórico no necesita filtros de fecha

    # ✅ SUMA SOLO CUOTAS PAGADAS
    gasto_cuotas = Cuota.objects.filter(**filtros_cuotas)\
        .aggregate(total=Sum('monto'))['total'] or 0

    # gastos normales
    gasto_diario = Gasto.objects.filter(**filtros)\
        .aggregate(total=Sum('monto'))['total'] or 0

    gasto_total = gasto_diario + gasto_cuotas
    saldo = ingreso_total - gasto_total
    saldo_rojo = saldo if saldo < 0 else None

    # ✅ SOLO GASTOS CON CUOTAS
    lista_cuotas = Gasto_fijo.objects.filter(
        usuario=request.user,
        cuotas__isnull=False
    ).exclude(cuotas=0).annotate(
        total_cuotas=Count('cuota'),
        cuotas_pagadas=Count('cuota', filter=Q(cuota__pagada=True))
    ).exclude(
        total_cuotas=F('cuotas_pagadas')  # 👈 elimina los completamente pagos
    )

    return render(request, 'core/index.html', {
        'ingreso': ingreso_total,
        'gasto_total': gasto_total,
        'saldo': saldo,
        'saldo_rojo': saldo_rojo,
        'titulo': titulo,
        'filtro_activo': filtro_tipo,
        'lista_cuotas': lista_cuotas,
    })

@require_POST
def toggle_cuota(request, cuota_id):
    cuota = Cuota.objects.get(id=cuota_id)
    cuota.pagada = not cuota.pagada
    cuota.save()

    return JsonResponse({'ok': True})