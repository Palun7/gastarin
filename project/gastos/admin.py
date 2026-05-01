from django.contrib import admin
from .models import Categoria, Categoria_ingreso, Gasto, Gasto_fijo, Ingreso, Cuota

admin.site.register(Categoria)
admin.site.register(Categoria_ingreso)
admin.site.register(Gasto)
admin.site.register(Gasto_fijo)
admin.site.register(Ingreso)
admin.site.register(Cuota)
