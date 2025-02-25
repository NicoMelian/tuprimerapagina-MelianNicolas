from django.db import models

# Create your models here.
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='articulos')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, related_name='comentarios', on_delete=models.CASCADE)
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor} a {self.articulo.titulo}"
