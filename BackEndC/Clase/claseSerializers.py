from rest_framework import serializers
from Clase.models import Aula, Grupo, Clase

class aulaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = "__all__"

class grupoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = "__all__"

class claseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = "__all__"