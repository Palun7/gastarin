from django.shortcuts import render
from gastos.models import Gasto, Gasto_fijo, Ingreso
from django.db.models import Sum
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def transformar_mes(numero):
    numero = str(numero)
    if numero == '1':
        return 'Enero'
    elif numero == '2':
        return 'Febrero'
    elif numero == '3':
        return 'Marzo'
    elif numero == '4':
        return 'Abril'
    elif numero == '5':
        return 'Mayo'
    elif numero == '6':
        return 'Junio'
    elif numero == '7':
        return 'Julio'
    elif numero == '8':
        return 'Agosto'
    elif numero == '9':
        return 'Septiembre'
    elif numero == '10':
        return 'Octubre'
    elif numero == '11':
        return 'Noviembre'
    elif numero == '12':
        return 'Diciembre'

@login_required
def index(request):
    hoy = timezone.now()

    # valores por defecto (si no pasan nada)
    year = request.GET.get('year') or hoy.year
    month = request.GET.get('month')
    day = request.GET.get('day')

    mes = transformar_mes(hoy.month)

    filtros = {
        'usuario': request.user,
        'fecha__year': year
    }

    if month:
        filtros['fecha__month'] = month

    if day:
        filtros['fecha__day'] = day

    # ingresos
    ingreso_total = Ingreso.objects.filter(**filtros)\
        .aggregate(total=Sum('monto'))['total'] or 0

    # gastos
    gasto_diario = Gasto.objects.filter(**filtros)\
        .aggregate(total=Sum('monto'))['total'] or 0

    # gastos fijos
    gasto_fijo = Gasto_fijo.objects.filter(**filtros)\
        .aggregate(total=Sum('monto'))['total'] or 0

    # saldo final
    saldo = ingreso_total - (gasto_diario + gasto_fijo)

    gasto_total = gasto_diario + gasto_fijo

    return render(request, 'core/index.html', {
        'ingreso': ingreso_total,
        'gasto_total': gasto_total,
        'saldo': saldo,
        'mes': mes,
    })
