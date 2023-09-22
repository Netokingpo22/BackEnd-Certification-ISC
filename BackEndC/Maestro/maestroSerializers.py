from rest_framework import serializers
from Maestro.models import Maestro

class maestroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Maestro
        fields = "__all__"