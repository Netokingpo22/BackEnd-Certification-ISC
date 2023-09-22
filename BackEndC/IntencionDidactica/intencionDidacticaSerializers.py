from rest_framework import serializers
from IntencionDidactica.models import IntencionDidactica

class intencionDidacticaSerializers(serializers.ModelSerializer):
    class Meta:
        model = IntencionDidactica
        fields = "__all__"