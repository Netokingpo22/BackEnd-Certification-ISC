from rest_framework import serializers
from Alumno.models import Alumno

class alumnoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = "__all__"