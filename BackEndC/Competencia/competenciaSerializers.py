from rest_framework import serializers

from Competencia.models import Competencia, ListaCompetencia

class competenciaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Competencia
        fields = "__all__"

class listaCompetenciaSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListaCompetencia
        fields = "__all__"