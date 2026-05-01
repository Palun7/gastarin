from django.contrib import admin
from .models import Categoria, Categoria_ingreso, Gasto, Ingreso

admin.site.register(Categoria)
admin.site.register(Categoria_ingreso)
admin.site.register(Gasto)
admin.site.register(Ingreso)
