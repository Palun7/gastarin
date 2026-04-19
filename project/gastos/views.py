from django.shortcuts import render

def ingresar_gasto(request):
    return render(request, 'gastos/ingresar-gastos.html')