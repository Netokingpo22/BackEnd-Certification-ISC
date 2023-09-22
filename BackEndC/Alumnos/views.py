from rest_framework.response import Response
from rest_framework.decorators import api_view
from Alumnos.alumnoSerializers import alumnoSerializers

from Alumnos.models import Alumnos

# Create your views here.


@api_view(['GET', 'POST'])
def alumnos_api_view(request):

    if request.method == 'GET':
        alumnos = Alumnos.objects.all()
        alumnosSerializer = alumnoSerializers(alumnos, many=True)
        return Response(alumnosSerializer.data)
    
    elif request.method == 'POST':
        alumnosSerializer = alumnoSerializers(data=request.data)
        if alumnosSerializer.is_valid():
            alumnosSerializer.save()
            return Response(alumnosSerializer.data)
        return Response(alumnosSerializer.errors)