from django.shortcuts import render
from .models import Usuario

def login_registro(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            pass
        elif 'registro' in request.POST:
            pass
    return render(request, 'usuarios/login-registro.html')