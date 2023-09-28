from rest_framework.response import Response
from rest_framework.decorators import api_view

from Alumno.models import Alumno, AlumnoClase, AlumnoTemaClase

from Alumno.alumnoSerializers import alumnoSerializers
from Alumno.alumnoSerializers import alumnoClaseSerializers
from Alumno.alumnoSerializers import alumnoTemaClaseSerializers

# Create your views here.


@api_view(['GET', 'POST'])
def alumno_api_view(request):

    if request.method == 'GET':
        alumno = Alumno.objects.all()
        alumnosSerializers = alumnoSerializers(alumno, many=True)
        return Response(alumnosSerializers.data)

    elif request.method == 'POST':
        alumnosSerializers = alumnoSerializers(data=request.data)
        if alumnosSerializers.is_valid():
            alumnosSerializers.save()
            return Response(alumnosSerializers.data)
        return Response(alumnosSerializers.errors)

@api_view(['GET', 'POST'])
def alumnoClase_api_view(request):

    if request.method == 'GET':
        alumnoClase = AlumnoClase.objects.all()
        alumnoCSerializers = alumnoClaseSerializers(alumnoClase, many=True)
        return Response(alumnoCSerializers.data)

    elif request.method == 'POST':
        alumnoCSerializers = alumnoClaseSerializers(data=request.data)
        if alumnoCSerializers.is_valid():
            alumnoCSerializers.save()
            return Response(alumnoCSerializers.data)
        return Response(alumnoCSerializers.errors)

@api_view(['GET', 'POST'])
def alumnoTemaClase_api_view(request):

    if request.method == 'GET':
        alumnoTemaClase = AlumnoTemaClase.objects.all()
        alumnoTCSerializers = alumnoTemaClaseSerializers(alumnoTemaClase, many=True)
        return Response(alumnoTCSerializers.data)

    elif request.method == 'POST':
        alalumnoTCSerializersumnoCSerializers = alumnoTemaClaseSerializers(data=request.data)
        if alumnoTCSerializers.is_valid():
            alumnoTCSerializers.save()
            return Response(alumnoTCSerializers.data)
        return Response(alumnoTCSerializers.errors)
