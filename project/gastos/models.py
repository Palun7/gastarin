from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from usuarios.models import Usuario

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

class Categoria_ingreso(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    icono = models.ImageField(upload_to='categorias_ingreso/', validators=[validar_tamano])

    class Meta:
        verbose_name = 'Categoría ingreso'
        verbose_name_plural = 'Categorías ingreso'

    def __str__(self):
        return self.nombre

class Gasto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
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
            return f'{self.usuario.username}: ${self.monto} - {self.nota}'
        else:
            return f'{self.usuario.username}: ${self.monto} - {self.categoria.nombre}'

class Ingreso(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=11, decimal_places=2)
    categoria = models.ForeignKey(Categoria_ingreso, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now)
    nota = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='ingresos/', blank=True, null=True)

    class Meta:
        verbose_name = 'Ingreso'
        verbose_name_plural = 'Ingresos'

    def __str__(self):
        if self.nota:
            return f'{self.usuario.username}: ${self.monto} - {self.nota}'
        else:
            return f'{self.usuario.username}: ${self.monto}'

class Gasto_fijo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=11, decimal_places=2)
    cuotas = models.IntegerField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now)
    nota = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='gastos_fijos/', blank=True, null=True)

    class Meta:
        verbose_name = 'Gasto Fijo'
        verbose_name_plural = 'Gastos Fijos'

    def __str__(self):
        if self.nota and not self.cuotas:
            return f'{self.usuario.username}: ${self.monto} - {self.nota}'
        elif self.cuotas and not self.nota:
            return f'{self.usuario.username}: ${self.monto} - {self.cuotas}'
        elif self.cuotas and self.nota:
            return f'{self.usuario.username}: ${self.monto} - {self.cuotas} - {self.nota}'
        else:
            return f'{self.usuario.username}: ${self.monto} - {self.categoria.nombre}'