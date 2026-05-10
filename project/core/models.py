from django.db import models
from usuarios.models import Usuario

class Recomendaciones(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30)
    texto = models.CharField(max_length=300)
    foto = models.ImageField(upload_to='recomendaciones/', null=True, blank=True)

    class Meta:
        verbose_name = 'Recomendacion'
        verbose_name_plural = 'Recomendaciones'

    def __str__(self):
        return f'{self.usuario} - {self.titulo}'