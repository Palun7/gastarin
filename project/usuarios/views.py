from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Usuario

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