from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('cuota/<int:cuota_id>/toggle/', views.toggle_cuota, name='toggle_cuota'),
]