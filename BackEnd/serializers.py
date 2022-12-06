from rest_framework import serializers
from BackEnd.models import Publicidad, Servicios, User, Categorias, Comentarios, Historial, ImagenesPublicadas, Usuarios, Lugares, Ciudades, Opiniones, lugaresFavoritos
    
class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ('id', 'UsuarioName', 'UsuarioEmail', 'UsuarioStatus', 'UrlImagen', 'Descripcion')

class LugaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugares
        fields = ('LugarId','LugarName','CategoriaId','Coordenadas','Ciudad','CodigoPostal','Horario','LugarStatus','Servicios','UrlImagen','Likes','Dislikes', 'Numero', 'Latitud', 'Longitud')

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
        
class CiudadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudades
        fields = ('CiudadId', 'CiudadName')
        
class UserSerializer(serializers.ModelSerializer):
     class Meta:
        model = User
        fields = ['id', 'UsuarioName', 'UsuarioEmail', 'UsuarioPassword', 'UsuarioStatus', 'UrlImagen', "Descripcion", "password"]

     def create(self, validated_data):
         password = validated_data.pop('UsuarioPassword', None)
         instance = self.Meta.model(**validated_data)
         if password is not None:
            instance.set_password(password)
         instance.save()
         return instance

class OpinionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opiniones
        fields = ('OpinionId','UsuarioId','LugarId','Comentario', 'UrlImagen', 'Like', 'Dislike')

class LugaresFavoritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = lugaresFavoritos
        fields = ('lugarFavoritoId','UsuarioID','LugarID')
        
class ServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields = ('ServicioId','Nombre','LugarId')
        
class PublicidadSerializer(serializers.ModelSerializer):
    class meta:
        model = Publicidad
        fields = ('PublicidadId', 'LugarId', 'LugarName', 'UrlImagen')