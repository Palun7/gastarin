from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('login_registro/', views.login_registro, name='login-registro'),
]