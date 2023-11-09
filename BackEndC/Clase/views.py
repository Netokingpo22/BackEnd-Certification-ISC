from rest_framework.response import Response

from rest_framework.decorators import api_view

from Clase.claseSerializers import aulaSerializers
from Clase.claseSerializers import grupoSerializers
from Clase.claseSerializers import claseSerializers

from Clase.models import Aula, Grupo, Clase

# Create your views here.


from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['POST', 'GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def aula_api_view(request):

    if request.method == 'GET':
        aula = Aula.objects.all()
        aulasSerializer = aulaSerializers(aula, many=True)
        return Response(aulasSerializer.data)

    elif request.method == 'POST':
        aulasSerializer = aulaSerializers(data=request.data)
        if aulasSerializer.is_valid():
            aulasSerializer.save()
            return Response(aulasSerializer.data)
        return Response(aulasSerializer.errors)


@api_view(['POST', 'GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def grupo_api_view(request):

    if request.method == 'GET':
        grupo = Grupo.objects.all()
        gruposSerializers = grupoSerializers(grupo, many=True)
        return Response(gruposSerializers.data)

    elif request.method == 'POST':
        gruposSerializers = grupoSerializers(data=request.data)
        if gruposSerializers.is_valid():
            gruposSerializers.save()
            return Response(gruposSerializers.data)
        return Response(gruposSerializers.errors)


@api_view(['POST', 'GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def clase_api_view(request):

    if request.method == 'GET':
        clase = Clase.objects.all()
        clasesSerializers = claseSerializers(clase, many=True)
        return Response(clasesSerializers.data)

    elif request.method == 'POST':
        clasesSerializers = claseSerializers(data=request.data)
        if clasesSerializers.is_valid():
            clasesSerializers.save()
            return Response(clasesSerializers.data)
        return Response(clasesSerializers.errors)
