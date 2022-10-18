from rest_framework import serializers
from BackEnd.models import Categorias, Comentarios, Historial, ImagenesPublicadas, Usuarios, Lugares
    
class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ('UsuarioId', 'UsuarioName', 'UsuarioApellidos', 'UsuarioEmail', 'UsuarioPassword', 'UsuarioTelefono', 'UsuarioStatus', 'UrlImagen')

class LugaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugares
        fields = ('LugarId','LugarName','CategoriaId','Coordenadas','CiudadId','CodigoPostal','Horario','LugarStatus','Servicios','UrlImagen','Likes','Dislikes')

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = ('CategoriaId','CategoriaName')
        
class HistorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historial
        fields = ('HistoricoId','LugarId','UsuarioId')
        
class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = ('ComentarioId','LugarId','UsuarioId','Comentario')

class ImagenesPublicadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenesPublicadas
        fields = ('ImagenId','LugarId','UsuarioId','UrlImagen')