from django.urls import path
from . import views

app_name = 'gastos'

urlpatterns = [
    path('ingresar_gastos/', views.ingresar_gasto, name='ingresar-gastos'),
    path('gastos/', views.gastos, name='gastos'),
    path('gasto-fijo/<int:id>/data/', views.gasto_fijo_data),
    path('gasto-fijo/<int:id>/editar/', views.editar_gasto_fijo),
    path('gasto-diario/<int:id>/data/', views.gasto_diario_data),
    path('gasto-diario/<int:id>/editar/', views.editar_gasto_diario),
    path('ingreso/<int:id>/data/', views.ingreso_data),
    path('ingreso/<int:id>/editar/', views.editar_ingreso),
]