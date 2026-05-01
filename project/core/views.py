from django.shortcuts import render
from gastos.models import Gasto, Gasto_fijo, Ingreso
from django.db.models import Sum
from django.utils import timezone
from django.contrib.auth.decorators import login_required


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

    # 👉 tipo de filtro (default: mes)
    filtro_tipo = request.GET.get('filtro', 'mes')

    # 👉 base de filtros
    filtros = {
        'usuario': request.user,
    }

    # 👉 aplicar filtros según tipo
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
        titulo = f"Año {hoy.year}"

    elif filtro_tipo == 'historico':
        titulo = "Histórico"

    else:
        # fallback por si viene algo raro
        filtros['fecha__year'] = hoy.year
        filtros['fecha__month'] = hoy.month
        titulo = transformar_mes(hoy.month)

    # 👉 consultas
    ingreso_total = Ingreso.objects.filter(**filtros)\
        .aggregate(total=Sum('monto'))['total'] or 0

    gasto_diario = Gasto.objects.filter(**filtros)\
        .aggregate(total=Sum('monto'))['total'] or 0

    gasto_fijo = Gasto_fijo.objects.filter(**filtros)\
        .aggregate(total=Sum('monto'))['total'] or 0

    # 👉 cálculos
    gasto_total = gasto_diario + gasto_fijo
    saldo = ingreso_total - gasto_total

    saldo_rojo = saldo if saldo < 0 else None

    return render(request, 'core/index.html', {
        'ingreso': ingreso_total,
        'gasto_total': gasto_total,
        'saldo': saldo,
        'saldo_rojo': saldo_rojo,
        'titulo': titulo,
        'filtro_activo': filtro_tipo,  # 👈 útil para el front
    })