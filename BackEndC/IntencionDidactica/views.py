from rest_framework.response import Response
from rest_framework.decorators import api_view
from IntencionDidactica.intencionDidacticaSerializers import intencionDidacticaSerializers

from IntencionDidactica.models import IntencionDidactica
# Create your views here.


@api_view(['GET', 'POST'])
def intencionDidactica_api_view(request):

    if request.method == 'GET':
        intencionD = IntencionDidactica.objects.all()
        intencionesDSerializers = intencionDidacticaSerializers(intencionD, many=True)
        return Response(intencionesDSerializers.data)
    
    elif request.method == 'POST':
        intencionesDSerializers = intencionDidacticaSerializers(data=request.data)
        if intencionesDSerializers.is_valid():
            intencionesDSerializers.save()
            return Response(intencionesDSerializers.data)
        return Response(intencionesDSerializers.errors)