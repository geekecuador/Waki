from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=25)
    class Meta:
        app_label = 'wak'
    def __str__(self):
        return self.nombre
    def __unicode__(self):
        return self.nombre

class Comentario(models.Model):
    feedback = models.TextField()
    class Meta:
        app_label = 'wak'
    def __str__(self):
        return self.feedback
    def __unicode__(self):
        return self.feedback

class Metodo(models.Model):
    metodo = models.CharField(max_length=25)
    class Meta:
        app_label = 'wak'

class Recompensa(models.Model):
    titulo = models.CharField(max_length=25)
    descripcion = models.TextField()
    class Meta:
        app_label = 'wak'

class Fondo(models.Model):
    fondo = models.DecimalField(default=0, max_digits=4, decimal_places=2)
    class Meta:
        app_label = 'wak'
class Puntaje(models.Model):
    puntos = models.IntegerField()
    class Meta:
        app_label = 'wak'
class Producto(models.Model):
    titulo = models.CharField(max_length=25)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to="imagenes/")
    oferta = models.DecimalField(default=0, max_digits=4, decimal_places=2)
    fecha = models.DateTimeField
    lon = models.FloatField()
    lat = models.FloatField()
    categoria = models.ForeignKey(Categoria)
    comentario = models.ForeignKey(Comentario, blank=True, null=True)
    class Meta:
        app_label = 'wak'

class Vaca(models.Model):
    titulo = models.CharField(max_length=25)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to="imagenes/")
    oferta = models.DecimalField(default=0, max_digits=4, decimal_places=2)
    fecha = models.DateTimeField()
    fecha_finalizacion = models.DateTimeField()
    class Meta:
        app_label = 'wak'
