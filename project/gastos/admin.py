from django.contrib import admin
from .models import Categoria, Gasto, Ingreso

admin.site.register(Categoria)
admin.site.register(Gasto)
admin.site.register(Ingreso)
