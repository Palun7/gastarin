from django.urls import path
from . import views

app_name = 'gastos'

urlpatterns = [
    path('ingresar_gastos/', views.ingresar_gasto, name='ingresar-gastos'),
    path('gastos/', views.gastos, name='gastos'),
]