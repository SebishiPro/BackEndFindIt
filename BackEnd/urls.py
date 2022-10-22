from django.urls import path
from BackEnd import views

urlpatterns = [
    path("usuarios", views.usuariosABC, name="usuariosABC"),
    path('usuarios/<int:id>', views.usuariosABC, name='usuariosABC'),
    path("lugares", views.lugaresABC, name="lugaresABC"),
    path('lugares/<int:id>', views.lugaresABC, name='lugaresABC'),
    path('lugares/<str:ciudad>', views.lugaresFiltro, name='lugaresFiltro'),
    path('usuarios/<int:id>/historial', views.historialUsuario, name='historial'),
    path('lugares/<int:id>/comentarios', views.comentarios, name='comentarios'),
    path('lugares/<int:id>/fotos', views.publicarFoto, name='fotos')
]