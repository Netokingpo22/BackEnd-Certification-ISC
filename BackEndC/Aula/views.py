from rest_framework.response import Response
from rest_framework.decorators import api_view
from Aula.aulaSerializers import aulaSerializers

from Aula.models import Aula

# Create your views here.


@api_view(['GET', 'POST'])
def aula_api_view(request):

    if request.method == 'GET':
        aula = Aula.objects.all()
        aulasSerializers = aulaSerializers(aula, many=True)
        return Response(aulasSerializers.data)
    
    elif request.method == 'POST':
        aulasSerializers = aulaSerializers(data=request.data)
        if aulasSerializers.is_valid():
            aulasSerializers.save()
            return Response(aulasSerializers.data)
        return Response(aulasSerializers.errors)