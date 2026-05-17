from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('login_registro/', views.login_registro, name='login-registro'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('categoria/<int:id>/data/', views.categoria_data),
    path('categoria/<int:id>/editar/', views.editar_categoria),
    path('categoria-ingreso/<int:id>/data/', views.categoria_ingreso_data),
    path('categoria-ingreso/<int:id>/editar/', views.editar_categoria_ingreso),
]