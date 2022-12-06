from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.    
class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    UsuarioName = models.CharField(max_length = 100)
    UsuarioEmail = models.CharField(max_length=100)
    UsuarioStatus = models.CharField(max_length = 100)
    UrlImagen = models.CharField(max_length = 100)
    Descripcion = models.CharField(max_length=100)
    
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
    Numero = models.IntegerField()
    Latitud = models.CharField(max_length = 100)
    Longitud = models.CharField(max_length = 100)
    
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
    
    
class Ciudades(models.Model):
    CiudadId = models.AutoField(primary_key=True)
    CiudadName = models.CharField(max_length=100)
    
class User(AbstractUser):
    UsuarioName = models.CharField(max_length = 100)
    UsuarioEmail = models.EmailField(unique=True)
    UsuarioPassword = models.CharField(max_length = 100)
    UsuarioStatus = models.CharField(max_length = 100)
    UrlImagen = models.CharField(max_length = 100)
    Descripcion = models.CharField(max_length=1000)
    password = models.CharField(max_length=100)
    
    
    USERNAME_FIELD: 'UsuarioEmail'
    REQUIRED_FIELDS = []

class Opiniones(models.Model):
    OpinionId = models.AutoField(primary_key=True)
    UsuarioId =  models.IntegerField()
    LugarId =  models.IntegerField()
    Comentario = models.CharField(max_length = 100)
    UrlImagen = models.CharField(max_length = 100)
    Like = models.IntegerField()
    Dislike = models.IntegerField()
    
class lugaresFavoritos(models.Model):
    lugarFavoritoId = models.AutoField(primary_key=True)
    UsuarioID = models.IntegerField()
    LugarID = models.IntegerField()
    
class Servicios(models.Model):
    ServicioId = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length = 100)
    LugarId = models.IntegerField()
    
class Publicidad(models.Model):
    PublicidadId = models.AutoField(primary_key=True)
    LugarId = models.IntegerField()
    LugarName = models.CharField(max_length=100)
    UrlImagen = models.CharField(max_length=100)