from rest_framework import serializers
from Usuario.models import Usuario

class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"