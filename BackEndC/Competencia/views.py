from rest_framework.response import Response
from rest_framework.decorators import api_view

from Competencia.models import Competencia, ListaCompetencia

from Competencia.competenciaSerializers import competenciaSerializers
from Competencia.competenciaSerializers import listaCompetenciaSerializers

# Create your views here.


@api_view(['GET', 'POST'])
def competencia_api_view(request):

    if request.method == 'GET':
        competencia = Competencia.objects.all()
        competenciaS = competenciaSerializers(competencia, many=True)
        return Response(competenciaS.data)

    elif request.method == 'POST':
        competenciaS = competenciaSerializers(data=request.data)
        if competenciaS.is_valid():
            competenciaS.save()
            return Response(competenciaS.data)
        return Response(competenciaS.errors)

@api_view(['GET', 'POST'])
def listaCompetencia_api_view(request):

    if request.method == 'GET':
        listaCompetencia = ListaCompetencia.objects.all()
        listaCSerializers = listaCompetenciaSerializers(listaCompetencia, many=True)
        return Response(listaCSerializers.data)

    elif request.method == 'POST':
        listaCSerializers = listaCompetenciaSerializers(data=request.data)
        if listaCSerializers.is_valid():
            listaCSerializers.save()
            return Response(listaCSerializers.data)
        return Response(listaCSerializers.errors)
