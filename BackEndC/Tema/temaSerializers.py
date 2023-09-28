from rest_framework import serializers

from Tema.models import Tema
from Tema.models import ActividadEnseñanza
from Tema.models import ActividadAprendizaje
from Tema.models import CompetenciaGenerica
from Tema.models import InstrumentoEvaluacion

class temaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tema
        fields = "__all__"

class actividadEnseñanzaSerializers(serializers.ModelSerializer):
    class Meta:
        model = ActividadEnseñanza
        fields = "__all__"

class actividadAprendizajeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ActividadAprendizaje
        fields = "__all__"
        
class competenciaGenericaSerializers(serializers.ModelSerializer):
    class Meta:
        model = CompetenciaGenerica
        fields = "__all__"
        
class instrumentoEvaluacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = InstrumentoEvaluacion
        fields = "__all__"