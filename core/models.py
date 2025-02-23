from django.db import models
from ckeditor.fields import RichTextField

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = RichTextField()  # Cambiado a RichTextField
    contenido = RichTextField()  # Cambiado a RichTextField
    imagen = models.ImageField(upload_to='noticias/')
    fecha_publicacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateField()
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='eventos/', blank=True, null=True)  # Nuevo campo para la imagen

    def __str__(self):
        return self.nombre
