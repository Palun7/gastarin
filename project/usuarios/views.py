from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Usuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import update_session_auth_hash
import os
from gastos.views import Categoria, Categoria_ingreso
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def logout_view(request):
    logout(request)
    return redirect('usuarios:login-registro')

def login_registro(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            username = request.POST.get('username_login')
            password = request.POST.get('password_login')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('core:index')
            else:
                return render(request, 'usuarios/login-registro.html', {'error_login': 'Usuario o contraseña incorrectos'})

        elif 'registro' in request.POST:
            if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                email = request.POST['email']
                telefono = request.POST['telefono']
                foto = request.FILES.get('foto')

                if Usuario.objects.filter(username=username).exists():
                    return render(request, 'usuarios/login-registro.html', {
                        'error': 'El usuario ya existe'
                    })

                if password == '' or username == '':
                    return render(request, 'usuarios/login-registro.html', {
                        'error': 'Por favor, complete los campos obligatorios'
                    })

                user = Usuario.objects.create_user(
                    username=username,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    telefono=telefono,
                    foto=foto,
                )

                login(request, user)
                return render(request, 'core/index.html', {
                    'exito': 'Usuario registrado exitosamente'
                })

    return render(request, 'usuarios/login-registro.html')

@login_required
def perfil(request):
    user = request.user
    categorias = Categoria.objects.filter(usuario=request.user)
    categorias_ingreso = Categoria_ingreso.objects.filter(usuario=request.user)

    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.telefono = request.POST.get('telefono')
        password_actual = request.POST.get('password_actual')
        password = request.POST.get('password')

        if password:
            if check_password(password_actual, user.password):
                user.password = make_password(password)
            else:
                return render(request, 'usuarios/perfil.html', {
                    'usuario': user,
                    'error': 'Contraseña actual incorrecta',
                    'categorias': categorias,
                    'categorias_ingreso': categorias_ingreso,
                })

        if request.FILES.get('foto'):
            if user.foto:
                if os.path.isfile(user.foto.path):
                    os.remove(user.foto.path)
            user.foto = request.FILES.get('foto')

        user.save()
        update_session_auth_hash(request, user)
        return redirect('usuarios:perfil')

    return render(request, 'usuarios/perfil.html', {
        'categorias': categorias,
        'categorias_ingreso': categorias_ingreso,
    })

def categoria_data(request, id):

    categoria = Categoria.objects.filter(id=id).first()
    h4 = 'Editar Categoria de Gastos'

    if not categoria:
        categoria = Categoria_ingreso.objects.filter(id=id).first()
        h4 = 'Editar Categoria de Ingresos'

    if not categoria:
        return JsonResponse({'error': 'Categoría no encontrada'}, status=404)

    return JsonResponse({
        'nombre': categoria.nombre,
        'icono': categoria.icono,
        'h4': h4,
    })

@require_POST
def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)

    if not categoria:
        categoria = Categoria_ingreso.objects.get(id=id)
        nombre = request.POST.get('nombre')
        icono = request.POST.get('icono')

        categoria.nombre = nombre
        categoria.icono = icono

        categoria.save()

        return JsonResponse({'ok': True})

    nombre = request.POST.get('nombre')
    icono = request.POST.get('icono')

    categoria.nombre = nombre
    categoria.icono = icono

    categoria.save()

    return JsonResponse({'ok': True})