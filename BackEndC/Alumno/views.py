from rest_framework.response import Response
from rest_framework.decorators import api_view
from Alumno.alumnoSerializers import alumnoSerializers

from Alumno.models import Alumno

# Create your views here.


@api_view(['GET', 'POST'])
def alumno_api_view(request):

    if request.method == 'GET':
        alumnos = Alumno.objects.all()
        alumnosSerializer = alumnoSerializers(alumnos, many=True)
        return Response(alumnosSerializer.data)
    
    elif request.method == 'POST':
        alumnosSerializer = alumnoSerializers(data=request.data)
        if alumnosSerializer.is_valid():
            alumnosSerializer.save()
            return Response(alumnosSerializer.data)
        return Response(alumnosSerializer.errors)