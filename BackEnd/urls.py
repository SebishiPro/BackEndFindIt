from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from BackEnd import views
from .views import RegisterView, LoginView, UserView, LogoutView, CambiarPass, lugaresFiltroBuscar

urlpatterns = [
    path('usuarios', views.usuariosABC, name='usuariosABC'),
    path('lugares', views.lugaresABC, name='lugaresABC'),
    path('usuarios/<int:id>', views.usuariosABC, name='usuariosABC'),
    path('lugares/<int:id>', views.lugaresABC, name='lugaresABC'),
    path('saveFile/', views.saveFile, name='fotos'),
    path('lugares/<str:ciudad>', views.lugaresFiltro, name='lugaresFiltro'),
    path('usuarios/<int:id>/historial', views.historialUsuario, name='historial'),
    path('lugares/<int:id>/comentarios', views.comentarios, name='comentarios'),
    path('opiniones/<int:idU>',views.opinionfiltrada, name='opinionesF'),
    path('opinionesTodas/<int:id>',views.opinionesABC, name='opinionesF'),
    path('opinionesPost/',views.OpionionesPost, name='opinionesPOST'),
    path('lugaresfavoritos/<int:idU>', views.insertarLugarFavorito, name='insertarLugarFavorito'),
    path('lugaresfavoritos/', views.insertarLugarFavorito, name='insertarLugarFavorito'),
    path('registro', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('inicio', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('resultados/<int:id>/<str:ciudad>', views.obtenerLugares, name='obtenerLugares'),
    path('servicios/<int:id>', views.serviciosABC, name='serviciosABC'),
    path('passCambio/<int:id>/<str:passw>', CambiarPass.as_view()),
    path('lugaresfiltrobuscar/<str:ciudad>', views.lugaresFiltroBuscar, name='lugaresfiltrobuscar'),
    path('ciudades/<int:id>', views.ciudadesABC, name='ciudadesABC')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)