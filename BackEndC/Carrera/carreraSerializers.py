from rest_framework import serializers
from Carrera.models import Carrera

class carreraSerializers(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = "__all__"