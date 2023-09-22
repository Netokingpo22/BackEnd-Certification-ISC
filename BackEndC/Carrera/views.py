from rest_framework.response import Response
from rest_framework.decorators import api_view
from Carrera.carreraSerializers import carreraSerializers

from Carrera.models import Carrera

# Create your views here.


@api_view(['GET', 'POST'])
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
        return Response(carrerasSerializers.errors)