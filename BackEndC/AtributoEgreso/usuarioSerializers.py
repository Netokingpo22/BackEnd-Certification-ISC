from rest_framework import serializers
from AtributoEgreso.models import AtributoEgreso, CriterioDesempeño, Indicador

class atributoEgresoSerializers(serializers.ModelSerializer):
    class Meta:
        model = AtributoEgreso
        fields = "__all__"

class criterioDesempeñoSerializers(serializers.ModelSerializer):
    class Meta:
        model = CriterioDesempeño
        fields = "__all__"

class indicadorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Indicador
        fields = "__all__"