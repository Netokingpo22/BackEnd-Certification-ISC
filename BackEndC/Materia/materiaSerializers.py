from rest_framework import serializers
from Materia.models import Materia, IntencionDidactica

class materiaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = "__all__"


class intencionDidacticaSerializers(serializers.ModelSerializer):
    class Meta:
        model = IntencionDidactica
        fields = "__all__"