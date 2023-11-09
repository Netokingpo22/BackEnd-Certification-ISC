from rest_framework.response import Response
from rest_framework.decorators import api_view
from Tema.temaSerializers import temaSerializers
from Tema.temaSerializers import actividadAprendizajeSerializers
from Tema.temaSerializers import actividadEnseñanzaSerializers
from Tema.temaSerializers import competenciaGenericaSerializers
from Tema.temaSerializers import instrumentoEvaluacionSerializers

from Tema.models import Tema
from Tema.models import ActividadAprendizaje
from Tema.models import ActividadEnseñanza
from Tema.models import CompetenciaGenerica
from Tema.models import InstrumentoEvaluacion

# Create your views here.


from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['POST', 'GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def tema_api_view(request):

    if request.method == 'GET':
        tema = Tema.objects.all()
        temasSerializers = temaSerializers(tema, many=True)
        return Response(temasSerializers.data)

    elif request.method == 'POST':
        temasSerializers = temaSerializers(data=request.data)
        if temasSerializers.is_valid():
            temasSerializers.save()
            return Response(temasSerializers.data)
        return Response(temasSerializers.errors)


@api_view(['POST', 'GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def actividadAprendizaje_api_view(request):

    if request.method == 'GET':
        actividadesAprendizaje = ActividadAprendizaje.objects.all()
        actividadesASerializers = actividadAprendizajeSerializers(
            actividadesAprendizaje, many=True)
        return Response(actividadesASerializers.data)

    elif request.method == 'POST':
        actividadesASerializers = actividadAprendizajeSerializers(
            data=request.data)
        if actividadesASerializers.is_valid():
            actividadesASerializers.save()
            return Response(actividadesASerializers.data)
        return Response(actividadesASerializers.errors)


@api_view(['POST', 'GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def actividadesEnseñanza_api_view(request):

    if request.method == 'GET':
        actividadesEnseñanza = ActividadEnseñanza.objects.all()
        actividadesESerializers = actividadEnseñanzaSerializers(
            actividadesEnseñanza, many=True)
        return Response(actividadesESerializers.data)

    elif request.method == 'POST':
        actividadesESerializers = actividadEnseñanzaSerializers(
            data=request.data)
        if actividadesESerializers.is_valid():
            actividadesESerializers.save()
            return Response(actividadesESerializers.data)
        return Response(actividadesESerializers.errors)


@api_view(['POST', 'GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def competenciaGenerica_api_view(request):

    if request.method == 'GET':
        competenciaGenerica = CompetenciaGenerica.objects.all()
        competenciaGSerializers = competenciaGenericaSerializers(
            competenciaGenerica, many=True)
        return Response(competenciaGSerializers.data)

    elif request.method == 'POST':
        competenciaGSerializers = competenciaGenericaSerializers(
            data=request.data)
        if competenciaGSerializers.is_valid():
            competenciaGSerializers.save()
            return Response(competenciaGSerializers.data)
        return Response(competenciaGSerializers.errors)


@api_view(['POST', 'GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def instrumentoEvaluacion_api_view(request):

    if request.method == 'GET':
        instrumentoEvaluacion = InstrumentoEvaluacion.objects.all()
        instrumentoESerializers = instrumentoEvaluacionSerializers(
            instrumentoEvaluacion, many=True)
        return Response(instrumentoESerializers.data)

    elif request.method == 'POST':
        instrumentoESerializers = instrumentoEvaluacionSerializers(
            data=request.data)
        if instrumentoESerializers.is_valid():
            instrumentoESerializers.save()
            return Response(instrumentoESerializers.data)
        return Response(instrumentoESerializers.errors)
