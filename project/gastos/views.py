from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Categoria, Gasto, Gasto_fijo, Ingreso, Categoria_ingreso, Cuota
from decimal import Decimal

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
    return render(request, 'gastos/gastos.html')