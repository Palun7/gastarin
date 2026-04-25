from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

def validar_tamano(archivo):
    limite = 5 * 1024 * 1024  # 5 MB
    if archivo.size > limite:
        raise ValidationError("El archivo es muy grande")

class Categoria(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    icono = models.ImageField(upload_to='categorias/', validators=[validar_tamano])

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre

class Gasto(models.Model):
    monto = models.DecimalField(max_digits=11, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now)
    nota = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='gastos/', blank=True, null=True)

    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'

    def __str__(self):
        if self.nota:
            return f'{self.monto} - {self.nota}'
        else:
            return f'{self.monto} - {self.categoria.nombre}'

class ingreso(models.Model):
    monto = models.DecimalField(max_digits=11, decimal_places=2)
    fecha = models.DateField(default=timezone.now)
    nota = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='ingresos/', blank=True, null=True)

    class Meta:
        verbose_name = 'Ingreso'
        verbose_name_plural = 'Ingresos'

    def __str__(self):
        if self.nota:
            return f'{self.monto} - {self.nota}'
        else:
            return f'{self.monto}'