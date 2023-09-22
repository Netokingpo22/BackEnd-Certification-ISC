from rest_framework import serializers
from Alumnos.models import Alumnos

class alumnoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alumnos
        fields = "__all__"