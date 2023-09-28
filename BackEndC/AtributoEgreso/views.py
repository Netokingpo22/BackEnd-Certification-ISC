from rest_framework.response import Response
from rest_framework.decorators import api_view

from AtributoEgreso.usuarioSerializers import atributoEgresoSerializers
from AtributoEgreso.usuarioSerializers import criterioDesempeñoSerializers
from AtributoEgreso.usuarioSerializers import indicadorSerializers

from AtributoEgreso.models import AtributoEgreso,CriterioDesempeño,Indicador

# Create your views here.


@api_view(['GET', 'POST'])
def atributoEgreso_api_view(request):

    if request.method == 'GET':
        atributoEgreso = AtributoEgreso.objects.all()
        atributoESerializers = atributoEgresoSerializers(atributoEgreso, many=True)
        return Response(atributoESerializers.data)
    
    elif request.method == 'POST':
        atributoESerializers = atributoEgresoSerializers(data=request.data)
        if atributoESerializers.is_valid():
            atributoESerializers.save()
            return Response(atributoESerializers.data)
        return Response(atributoESerializers.errors)

@api_view(['GET', 'POST'])
def criterioDesempeño_api_view(request):

    if request.method == 'GET':
        criterioDesempeño = CriterioDesempeño.objects.all()
        criterioDSerializers = criterioDesempeñoSerializers(criterioDesempeño, many=True)
        return Response(criterioDSerializers.data)
    
    elif request.method == 'POST':
        criterioDSerializers = criterioDesempeñoSerializers(data=request.data)
        if criterioDSerializers.is_valid():
            criterioDSerializers.save()
            return Response(criterioDSerializers.data)
        return Response(criterioDSerializers.errors)

@api_view(['GET', 'POST'])
def indicador_api_view(request):

    if request.method == 'GET':
        indicador = Indicador.objects.all()
        indicadoresSerializers = indicadorSerializers(indicador, many=True)
        return Response(indicadoresSerializers.data)
    
    elif request.method == 'POST':
        indicadoresSerializers = indicadorSerializers(data=request.data)
        if indicadoresSerializers.is_valid():
            indicadoresSerializers.save()
            return Response(indicadoresSerializers.data)
        return Response(indicadoresSerializers.errors)