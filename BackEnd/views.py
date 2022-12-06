from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from BackEnd.models import Comentarios, Historial, ImagenesPublicadas, Lugares, Usuarios, Opiniones, Ciudades
from BackEnd.serializers import ComentariosSerializer, HistorialSerializer, ImagenesPublicadasSerializer, LugaresSerializer, UsuariosSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .serializers import CiudadesSerializer, LugaresFavoritosSerializer, OpinionesSerializer, ServiciosSerializer, UserSerializer
from rest_framework import generics 
from .models import Servicios, User, lugaresFavoritos
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from django.core.files.storage import default_storage
from datetime import date


# Create your views here.
########################################################################################################################################
@csrf_exempt #AQUI VAN ESTAR LAS FUNCIONE PARA USUARIOS
def usuariosABC(request,id=0):
    if request.method=='POST':#AQUI SE INTRODUCEN LOS NUEVOS USUARIOS 
        informacion = JSONParser().parse(request)
        serializer = UsuariosSerializer(data=informacion)
        if serializer.is_valid():
            serializer.save() #EL ID ESTA EN AUTOMATICO POR LO QUE NO ES NECESARIO PROPORCIONAR ALGUNO
            return JsonResponse("Added Succesfully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='GET':#AQUI SE OBTIENEN LOS USUARIOS REGRISTRADOS EN LA BASE DE DATOS, PUEDE SER POR ID O TODOS EN GENERAL DANDOLE VALOR DE 0 AL ID
        if(id>0):
            informacion=list(Usuarios.objects.filter(id=id).values())
            if len(informacion)>0:
                return JsonResponse(informacion, safe=False)
            else:
                return JsonResponse("No hay ningun usuario con ese id", safe=False)
        elif(id==0):
            informacion = Usuarios.objects.all()
            serializer = UsuariosSerializer(informacion, many =True)
            return JsonResponse(serializer.data, safe=False)
    elif request.method=='PUT':#AQUI SE PUEDE MODIFICAR ALGUN USUARIO POR MEDIO DE SU ID
        informacion_id = JSONParser().parse(request)
        informacion=Usuarios.objects.get(id=id)
        serializer=UsuariosSerializer(informacion, data = informacion_id)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Update Succesfully!!", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':#AQUI SE ELIMINARAN LOS USUARIOS QUE ESTEN EN LA BASE DE DATOS POR MEDIO DE SU ID
        informacion=Usuarios.objects.get(id=id)
        informacion.delete()
        return JsonResponse("Deleted Succesfully!!", safe=False)
@csrf_exempt
def historialUsuario(request,id=0):
    if request.method=='POST':#AQUI SE INTRODUCEN LOS LUGARES QUE HA VISITADO UN USUARIO 
        informacion = JSONParser().parse(request)
        serializer = HistorialSerializer(data=informacion)
        if serializer.is_valid():
            serializer.save() #EL ID ESTA EN AUTOMATICO POR LO QUE NO ES NECESARIO PROPORCIONAR ALGUNO
            return JsonResponse("Added Succesfully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='GET':#AQUI SE PUEDE CONSULTAR LOS LUGARES EN LOS QUE ESTUVO UN USUARIO, EN EL FRONT SE DEFINIRA QUE ES LO QUE SE LE MOSTRARA AL USUARIO
        if(id>0):
            informacion=list(Historial.objects.filter(UsuarioId=id).values())
            if len(informacion)>0:
                return JsonResponse(informacion, safe=False)
            else:
                return JsonResponse("No hay ningun historial para este usuario", safe=False)
##########################################################################################################
##########################################################################################################


@csrf_exempt #AQUI VAN ESTAR LAS FUNCIONES PARA LUGARES
def lugaresABC(request,id=0):
    if request.method=='POST':#AQUI SE INTRODUCEN LOS NUEVOS LUGARES 
        informacion = JSONParser().parse(request)
        serializer = LugaresSerializer(data=informacion)
        if serializer.is_valid():
            serializer.save() #EL ID ESTA EN AUTOMATICO POR LO QUE NO ES NECESARIO PROPORCIONAR ALGUNO
            return JsonResponse("Added Succesfully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='GET':#AQUI SE OBTIENEN LOS LUGARES REGRISTRADOS EN LA BASE DE DATOS, PUEDE SER POR ID O TODOS EN GENERAL DANDOLE VALOR DE 0 AL ID
        if(id>0):
            informacion=list(Lugares.objects.filter(LugarId=id).values())
            if len(informacion)>0:
                return JsonResponse(informacion, safe=False)
            else:
                return JsonResponse("No hay ningun lugar con ese id", safe=False)
        elif(id==0):
            informacion = Lugares.objects.all()
            serializer = LugaresSerializer(informacion, many =True)
            return JsonResponse(serializer.data, safe=False)
    elif request.method=='PUT':#AQUI SE PUEDE MODIFICAR ALGUN LUGAR POR MEDIO DE SU ID
        informacion_id = JSONParser().parse(request)
        informacion=Lugares.objects.get(LugarId=id)
        serializer=LugaresSerializer(informacion, data = informacion_id)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Update Succesfully!!", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':#AQUI SE ELIMINARAN LOS LUGARES QUE ESTEN EN LA BASE DE DATOS POR MEDIO DE SU ID
        informacion=Lugares.objects.get(LugarId=id)
        informacion.delete()
        return JsonResponse("Deleted Succesfully!!", safe=False)
@csrf_exempt
def lugaresFiltro(request,ciudad=''):
    if request.method=='GET':
        informacion=list(Lugares.objects.filter(Ciudad=ciudad).values())
        return JsonResponse(informacion, safe=False)
    
@csrf_exempt
def lugaresFiltroBuscar(request,ciudad=''):
    if request.method=='GET':
        informacion=list(Ciudades.objects.filter(CiudadName__contains=ciudad).values())
        if len(informacion)>0:
            return JsonResponse(informacion, safe=False)
        else:
            return JsonResponse("No hay ciudades", safe=False)
##########################################################################################################
##########################################################################################################


@csrf_exempt #FUNCIONES PARA LOS COMENTARIOS
def comentarios(request,id=0):
    if request.method=='POST':#AQUI SE INTRODUCIRAN COMENTARIOS
        informacion = JSONParser().parse(request)
        serializer = ComentariosSerializer(data=informacion)
        if serializer.is_valid():
            serializer.save() #EL ID ESTA EN AUTOMATICO POR LO QUE NO ES NECESARIO PROPORCIONAR ALGUNO
            return JsonResponse("Added Succesfully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='GET':
        informacion=list(Comentarios.objects.filter(LugarId=id).values())
        return JsonResponse(informacion, safe=False)
##########################################################################################################
##########################################################################################################

@csrf_exempt 
def saveFile(request):
    today = date.today()
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)
        
    return JsonResponse(file_name, safe=False)
##########################################################################################################
##########################################################################################################
##COOKIES, INICIO DE SESION Y REGISTRO HECHO POR JUDD
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    
    def post(self, request):
        email = request.data['UsuarioEmail']
        password = request.data['UsuarioPassword']
         
        user = User.objects.filter(UsuarioEmail=email).first()

        if user is None:
            raise AuthenticationFailed('Usuario no encontrado!')

        if not user.check_password(password):
            raise AuthenticationFailed('Contrasena incorrecta.')
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
    
        encoded = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        response.set_cookie(key='jwt', value=encoded, httponly=True)
        response.data = {
            'jwt': encoded
        }

        return response

class UserView(APIView):
    def get(self, request):
        #/inicio para obtener el ID del usuario logueado
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Aun no ha iniciado sesion...')

        try:
            payload = jwt.decode(token, 'secret', algorithms='HS256')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Aun no ha iniciado sesion...')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    def post (self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
    
class CambiarPass(APIView):
    def put(self, request, id='',passw=''):
        u = User.objects.get(id=id)
        u.set_password(passw)
        u.save()
        
        response = Response()
        response.data = {
            'message': 'Contraseña cambiada'
        }
        return response


@csrf_exempt
def opinionesABC(request, id=0):
    if request.method == 'GET':
        if(id>0):
            informacion=list(Opiniones.objects.filter(LugarId=id).values())
            if len(informacion)>0:
                return JsonResponse(informacion, safe=False)
            else:
                return JsonResponse("No hay opiniones de ese usuario.", safe=False)
            ##########################################################################
@csrf_exempt
def opinionfiltrada(request,idU=0):
    if request.method == 'GET':
        if(idU>0):
            informacion=list(Opiniones.objects.filter(UsuarioId=idU).values())
            if len(informacion)>0:
                return JsonResponse(informacion, safe=False)
            else:
                return JsonResponse("No hay opiniones de ese usuario.", safe=False)
        elif(idU==0):
            informacion = Opiniones.objects.all()
            serializer = OpinionesSerializer(informacion, many =True)
            return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def insertarLugarFavorito(request,idU=0):
    if request.method=='POST':#AQUI SE INTRODUCEN LOS LUGARES FAVORITOS
        informacion = JSONParser().parse(request)
        serializer = LugaresFavoritosSerializer(data=informacion)
        if serializer.is_valid():
            serializer.save() #EL ID ESTA EN AUTOMATICO POR LO QUE NO ES NECESARIO PROPORCIONAR ALGUNO
            return JsonResponse("Added Succesfully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'GET':
        if(idU>0):
            informacion=list(lugaresFavoritos.objects.filter(UsuarioID=idU).values())
            if len(informacion)>0:
                return JsonResponse(informacion, safe=False)
            else:
                return JsonResponse("No hay opiniones de ese usuario.", safe=False)
        elif(idU==0):
            informacion = lugaresFavoritos.objects.all()
            serializer = LugaresFavoritosSerializer(informacion, many =True)
            return JsonResponse(serializer.data, safe=False)
# Resultados
@csrf_exempt
def obtenerLugares(request, id=0, ciudad=''):
    if request.method=='GET':
        if(id>0):
            informacion=list(Lugares.objects.filter(CategoriaId=id, Ciudad=ciudad).values())
            if len(informacion)>0:
                return JsonResponse(informacion, safe=False)
            else:
                return JsonResponse("No hay lugares registrados en dicha ciudad.", safe=False)


@csrf_exempt #AQUI VAN ESTAR LAS FUNCIONES PARA LUGARES
def serviciosABC(request, id=0):
    if request.method=='POST':#AQUI SE INTRODUCEN LOS NUEVOS LUGARES 
        informacion = JSONParser().parse(request)
        serializer = ServiciosSerializer(data=informacion)
        if serializer.is_valid():
            serializer.save() #EL ID ESTA EN AUTOMATICO POR LO QUE NO ES NECESARIO PROPORCIONAR ALGUNO
            return JsonResponse("Added Succesfully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='GET':#AQUI SE OBTIENEN LOS LUGARES REGRISTRADOS EN LA BASE DE DATOS, PUEDE SER POR ID O TODOS EN GENERAL DANDOLE VALOR DE 0 AL ID
        if(id>0):
            informacion=list(Servicios.objects.filter(LugarId=id).values())
            if len(informacion)>0:
                return JsonResponse(informacion, safe=False)
            else:
                return JsonResponse("No hay ningun lugar con con ese id servicio", safe=False)
        elif(id==0):
            informacion = Servicios.objects.all()
            serializer = ServiciosSerializer(informacion, many =True)
            return JsonResponse(serializer.data, safe=False)
        
@csrf_exempt
def OpionionesPost(request):
    if request.method == 'POST':
        informacion = JSONParser().parse(request)
        serializer = OpinionesSerializer(data=informacion)
        if serializer.is_valid():
            serializer.save() #EL ID ESTA EN AUTOMATICO POR LO QUE NO ES NECESARIO PROPORCIONAR ALGUNO
            return JsonResponse("Added Succesfully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)

##########################################################################################################
##########################################################################################################


@csrf_exempt #AQUI VAN ESTAR LAS FUNCIONES PARA CIUDADES
def ciudadesABC(request,id=0):
    if request.method=='POST':#AQUI SE INTRODUCEN LOS NUEVOS CIUDADES 
        informacion = JSONParser().parse(request)
        serializer = CiudadesSerializer(data=informacion)
        if serializer.is_valid():
            serializer.save() #EL ID ESTA EN AUTOMATICO POR LO QUE NO ES NECESARIO PROPORCIONAR ALGUNO
            return JsonResponse("Added Succesfully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='GET':#AQUI SE OBTIENEN LOS CIUDADES REGRISTRADOS EN LA BASE DE DATOS, PUEDE SER POR ID O TODOS EN GENERAL DANDOLE VALOR DE 0 AL ID
        if(id>0):
            informacion=list(Ciudades.objects.filter(CiudadId=id).values())
            if len(informacion)>0:
                return JsonResponse(informacion, safe=False)
            else:
                return JsonResponse("No hay ninguna ciudad con ese id", safe=False)
        elif(id==0):
            informacion = Ciudades.objects.all()
            serializer = CiudadesSerializer(informacion, many =True)
            return JsonResponse(serializer.data, safe=False)
    elif request.method=='PUT':#AQUI SE PUEDE MODIFICAR ALGUNA CIUDAD POR MEDIO DE SU ID
        informacion_id = JSONParser().parse(request)
        informacion=Ciudades.objects.get(CiudadId=id)
        serializer=CiudadesSerializer(informacion, data = informacion_id)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Update Succesfully!!", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':#AQUI SE ELIMINARAN LAS CIUDADES QUE ESTEN EN LA BASE DE DATOS POR MEDIO DE SU ID
        informacion=Ciudades.objects.get(CiudadId=id)
        informacion.delete()
        return JsonResponse("Deleted Succesfully!!", safe=False)