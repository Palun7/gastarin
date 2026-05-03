from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Categoria, Gasto, Gasto_fijo, Ingreso, Categoria_ingreso, Cuota
from decimal import Decimal
from django.utils import timezone
from django.http import JsonResponse
from core.views import transformar_mes
import json
from django.views.decorators.http import require_POST

@login_required
def ingresar_gasto(request):

    categorias = Categoria.objects.filter(usuario=request.user)
    categorias_ingreso = Categoria_ingreso.objects.filter(usuario=request.user)

    if request.method == 'POST' and 'nombre_categoria' in request.POST:
        usuario = request.user
        nombre = request.POST.get('nombre_categoria').capitalize()
        icono = request.POST.get('icono') or "📁"  # default

        Categoria.objects.create(
            usuario=usuario,
            nombre=nombre,
            icono=icono
        )
        return redirect('gastos:ingresar-gastos')
    elif request.method == 'POST' and 'nombre_categoria_ingreso' in request.POST:
        usuario = request.user
        nombre = request.POST.get('nombre_categoria_ingreso').capitalize()
        icono = request.POST.get('icono') or "📁"  # default

        Categoria_ingreso.objects.create(
            usuario=usuario,
            nombre=nombre,
            icono=icono
        )
        return redirect('gastos:ingresar-gastos')

    if 'gasto_diario' in request.POST:
        usuario = request.user
        monto = request.POST.get('monto')
        categoria_id = request.POST.get('categoria')
        fecha = request.POST.get('fecha')
        nota = request.POST.get('nota')
        foto = request.FILES.get('foto')


        categoria = Categoria.objects.get(id=categoria_id)

        Gasto.objects.create(
            usuario=usuario,
            monto=monto,
            categoria=categoria,
            fecha=fecha,
            nota=nota,
            foto=foto,
        )
        return redirect('core:index')
    elif 'gasto_fijo' in request.POST:
        usuario = request.user
        monto = Decimal(request.POST.get('monto'))
        cuotas = request.POST.get('cuotas')
        categoria_id = request.POST.get('categoria')
        fecha = request.POST.get('fecha')
        nota = request.POST.get('nota')
        foto = request.FILES.get('foto')

        categoria = Categoria.objects.get(id=categoria_id)

        # 👉 crear el gasto fijo
        gasto = Gasto_fijo.objects.create(
            usuario=usuario,
            monto=monto,
            cuotas=cuotas if cuotas else None,
            categoria=categoria,
            fecha=fecha,
            nota=nota,
            foto=foto,
        )

        # 👉 si tiene cuotas, crearlas
        if cuotas:
            cuotas = int(cuotas)
            monto_cuota = monto / cuotas

            for i in range(1, cuotas + 1):
                Cuota.objects.create(
                    gasto=gasto,
                    numero=i,
                    monto=round(monto_cuota, 2)
                )

        return redirect('core:index')
    elif 'ingreso' in request.POST:
        usuario = request.user
        monto = request.POST.get('monto')
        categoria_id = request.POST.get('categoria')
        fecha = request.POST.get('fecha')
        nota = request.POST.get('nota')
        foto = request.FILES.get('foto')


        categoria = Categoria_ingreso.objects.get(id=categoria_id)

        Ingreso.objects.create(
            usuario=usuario,
            monto=monto,
            categoria=categoria,
            fecha=fecha,
            nota=nota,
            foto=foto,
        )
        return redirect('core:index')


    return render(request, 'gastos/ingresar-gastos.html', {'categorias': categorias, 'categorias_ingreso': categorias_ingreso})

@login_required
def gastos(request):
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

    gastos_fijos = Gasto_fijo.objects.filter(**filtros)

    categorias = Categoria.objects.filter(usuario=request.user)

    return render(request, 'gastos/gastos.html', {
        'gastos_fijos':gastos_fijos,
        'filtro_activo': filtro_tipo,
        'categorias': categorias,
        })

def gasto_fijo_data(request, id):
    gasto = Gasto_fijo.objects.get(id=id)

    return JsonResponse({
        'monto': float(gasto.monto),
        'cuotas': gasto.cuotas,
        'fecha': gasto.fecha.strftime('%Y-%m-%d'),
        'nota': gasto.nota,
        'categoria': gasto.categoria.id, # type:ignore
    })

@require_POST
def editar_gasto_fijo(request, id):
    gasto = Gasto_fijo.objects.get(id=id)

    monto = Decimal(request.POST.get('monto'))
    cuotas = request.POST.get('cuotas')
    fecha = request.POST.get('fecha')
    nota = request.POST.get('nota')
    categoria_id = request.POST.get('categoria')
    foto = request.FILES.get('foto')

    print(foto)

    gasto.monto = monto
    gasto.fecha = fecha
    gasto.nota = nota

    # categoría
    if categoria_id:
        gasto.categoria_id = int(categoria_id) #type:ignore

    # foto
    if foto:
        gasto.foto = foto

    if request.POST.get('eliminar_foto'):
        gasto.foto.delete()

    # cuotas
    nuevas_cuotas = int(cuotas) if cuotas else None

    if gasto.cuotas != nuevas_cuotas:
        gasto.cuotas = nuevas_cuotas

        # borrar cuotas viejas
        gasto.cuota_set.all().delete() #type:ignore

        # recrear
        if nuevas_cuotas:
            monto_cuota = monto / nuevas_cuotas

            for i in range(1, nuevas_cuotas + 1):
                Cuota.objects.create(
                    gasto=gasto,
                    numero=i,
                    monto=round(monto_cuota, 2)
                )

    gasto.save()

    return JsonResponse({'ok': True})