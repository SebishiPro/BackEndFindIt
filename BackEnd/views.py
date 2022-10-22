from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from BackEnd.models import Comentarios, Historial, ImagenesPublicadas, Lugares, Usuarios
from BackEnd.serializers import ComentariosSerializer, HistorialSerializer, ImagenesPublicadasSerializer, LugaresSerializer, UsuariosSerializer
from django.views.decorators.csrf import csrf_exempt

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
            informacion=list(Usuarios.objects.filter(UsuarioId=id).values())
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
        informacion=Usuarios.objects.get(UsuarioId=informacion_id['UsuarioId'])
        serializer=UsuariosSerializer(informacion, data = informacion_id)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Update Succesfully!!", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':#AQUI SE ELIMINARAN LOS USUARIOS QUE ESTEN EN LA BASE DE DATOS POR MEDIO DE SU ID
        informacion_id=JSONParser().parse(request)
        informacion=Usuarios.objects.get(UsuarioId=informacion_id['UsuarioId'])
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
        informacion=Lugares.objects.get(LugarId=informacion_id['LugarId'])
        serializer=LugaresSerializer(informacion, data = informacion_id)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Update Succesfully!!", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':#AQUI SE ELIMINARAN LOS LUGARES QUE ESTEN EN LA BASE DE DATOS POR MEDIO DE SU ID
        informacion_id=JSONParser().parse(request)
        informacion=Lugares.objects.get(LugarId=informacion_id['LugarId'])
        informacion.delete()
        return JsonResponse("Deleted Succesfully!!", safe=False)
@csrf_exempt
def lugaresFiltro(request,ciudad=''):
    if request.method=='GET':
        informacion=list(Lugares.objects.filter(Ciudad=ciudad).values())
        return JsonResponse(informacion, safe=False)
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

@csrf_exempt #FUNCIONES PARA FOTOS
def publicarFoto(request,id):
    if request.method=='POST':#AQUI SE INTRODUCIRAN COMENTARIOS
        informacion = JSONParser().parse(request)
        serializer = ImagenesPublicadasSerializer(data=informacion)
        if serializer.is_valid():
            serializer.save() #EL ID ESTA EN AUTOMATICO POR LO QUE NO ES NECESARIO PROPORCIONAR ALGUNO
            return JsonResponse("Added Succesfully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='GET':
        informacion=list(ImagenesPublicadas.objects.filter(LugarId=id).values())
        return JsonResponse(informacion, safe=False)