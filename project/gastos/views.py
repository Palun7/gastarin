from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Categoria, Gasto, ingreso

@login_required
def ingresar_gasto(request):
    if request.method == 'POST' and 'nombre' in request.POST:
        nombre = request.POST.get('nombre').capitalize()
        icono = request.POST.get('icono') or "📁"  # default

        Categoria.objects.create(
            nombre=nombre,
            icono=icono
        )
        return redirect('gastos:ingresar-gastos')


    categorias = Categoria.objects.all()

    return render(request, 'gastos/ingresar-gastos.html', {'categorias': categorias})

@login_required
def gastos(request):
    return render(request, 'gastos/gastos.html')