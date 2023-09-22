from rest_framework import serializers
from Aula.models import Aula

class aulaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = "__all__"