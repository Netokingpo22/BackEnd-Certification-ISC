from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from Carrera.carreraSerializers import carreraSerializers

from Carrera.models import Carrera

# Create your views here.


from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['POST', 'GET'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def carrera_api_view(request):

    if request.method == 'GET':
        carrera = Carrera.objects.all()
        carrerasSerializers = carreraSerializers(carrera, many=True)
        return Response(carrerasSerializers.data)
    
    elif request.method == 'POST':
        carrerasSerializers = carreraSerializers(data=request.data)
        if carrerasSerializers.is_valid():
            carrerasSerializers.save()
            return Response(carrerasSerializers.data)
        return Response({"detail": "not found"}, status=status.HTTP_404_NOT_FOUND)