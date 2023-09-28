from rest_framework import serializers

from Alumno.models import Alumno, AlumnoClase, AlumnoTemaClase

class alumnoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = "__all__"

class alumnoClaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = AlumnoClase
        fields = "__all__"

class alumnoTemaClaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = AlumnoTemaClase
        fields = "__all__"