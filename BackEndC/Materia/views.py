from rest_framework.response import Response
from rest_framework.decorators import api_view
from Materia.materiaSerializers import materiaSerializers, intencionDidacticaSerializers

from Materia.models import Materia, IntencionDidactica

# Create your views here.


@api_view(['GET', 'POST'])
def materia_api_view(request):

    if request.method == 'GET':
        materia = Materia.objects.all()
        materiasSerializer = materiaSerializers(materia, many=True)
        return Response(materiasSerializer.data)
    
    elif request.method == 'POST':
        materiasSerializer = materiaSerializers(data=request.data)
        if materiasSerializer.is_valid():
            materiasSerializer.save()
            return Response(materiasSerializer.data)
        return Response(materiasSerializer.errors)
    
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