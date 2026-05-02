from django.db import models
from django.utils import timezone
from usuarios.models import Usuario

class Categoria(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, unique=True)
    icono = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return f'{self.nombre} {self.icono}'

class Categoria_ingreso(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, unique=True)
    icono = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Categoría ingreso'
        verbose_name_plural = 'Categorías ingreso'

    def __str__(self):
        return f'{self.nombre} {self.icono}'

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
            return f'{self.usuario.username}: ${self.monto} {self.categoria.icono} - {self.nota}'
        else:
            return f'{self.usuario.username}: ${self.monto} {self.categoria.icono} - {self.categoria.nombre}'

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
            return f'{self.usuario.username}: ${self.monto} {self.categoria.icono} - {self.nota}'
        else:
            return f'{self.usuario.username}: ${self.monto} {self.categoria.icono}'

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
            return f'{self.usuario.username}: ${self.monto} {self.categoria.icono} - {self.nota}'
        elif self.cuotas and not self.nota:
            return f'{self.usuario.username}: ${self.monto} {self.categoria.icono} - {self.cuotas}'
        elif self.cuotas and self.nota:
            return f'{self.usuario.username}: ${self.monto} {self.categoria.icono} - {self.cuotas} - {self.nota}'
        else:
            return f'{self.usuario.username}: ${self.monto} {self.categoria.icono} - {self.categoria.nombre}'

class Cuota(models.Model):
    gasto = models.ForeignKey(Gasto_fijo, on_delete=models.CASCADE)
    numero = models.IntegerField()
    monto = models.DecimalField(max_digits=11, decimal_places=2)
    pagada = models.BooleanField(default=False)

    class Meta:
            verbose_name = 'Cuota'
            verbose_name_plural = 'Cuotas'

    def __str__(self):
        return f'{self.gasto} - Cuota {self.numero}'