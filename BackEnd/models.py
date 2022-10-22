from django.db import models

# Create your models here.    
class Usuarios(models.Model):
    UsuarioId = models.AutoField(primary_key=True)
    UsuarioName = models.CharField(max_length = 100)
    UsuarioApellidos = models.CharField(max_length = 100)
    UsuarioEmail = models.CharField(max_length=100)
    UsuarioPassword = models.CharField(max_length = 100)
    UsuarioTelefono = models.CharField(max_length = 10)
    UsuarioStatus = models.CharField(max_length = 100)
    UrlImagen = models.CharField(max_length = 100)
    
class Lugares(models.Model):
    LugarId = models.AutoField(primary_key=True)
    LugarName = models.CharField(max_length = 100)
    CategoriaId = models.CharField(max_length = 100)
    Coordenadas = models.CharField(max_length=100)
    Ciudad = models.CharField(max_length = 100)
    CodigoPostal = models.CharField(max_length = 100)
    Horario = models.CharField(max_length = 100)
    LugarStatus = models.CharField(max_length = 100)
    Servicios = models.CharField(max_length = 100)
    UrlImagen = models.CharField(max_length = 100)
    Likes = models.BigIntegerField()
    Dislikes = models.BigIntegerField()
    
class Categorias(models.Model):
    CategoriaId = models.AutoField(primary_key=True)
    CategoriaName = models.CharField(max_length = 100)
    
class Historial(models.Model):
    HistoricoId = models.AutoField(primary_key=True)
    LugarId = models.CharField(max_length = 100)
    UsuarioId = models.CharField(max_length = 100)
    
class Comentarios(models.Model):
    ComentarioId = models.AutoField(primary_key=True)
    LugarId = models.CharField(max_length = 100)
    UsuarioId = models.CharField(max_length = 100)
    Comentario = models.CharField(max_length = 100)
    
class ImagenesPublicadas(models.Model):
    ImagenId = models.AutoField(primary_key=True)
    LugarId = models.CharField(max_length = 100)
    UsuarioId = models.CharField(max_length = 100)
    UrlImagen = models.CharField(max_length = 100)