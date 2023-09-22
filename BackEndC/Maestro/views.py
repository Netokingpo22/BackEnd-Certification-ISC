from rest_framework.response import Response
from rest_framework.decorators import api_view
from Maestro.maestroSerializers import maestroSerializers

from Maestro.models import Maestro

# Create your views here.


@api_view(['GET', 'POST'])
def maestro_api_view(request):

    if request.method == 'GET':
        maestro = Maestro.objects.all()
        maestrosSerializer = maestroSerializers(maestro, many=True)
        return Response(maestrosSerializer.data)
    
    elif request.method == 'POST':
        maestrosSerializer = maestroSerializers(data=request.data)
        if maestrosSerializer.is_valid():
            maestrosSerializer.save()
            return Response(maestrosSerializer.data)
        return Response(maestrosSerializer.errors)