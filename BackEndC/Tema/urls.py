from django.urls import path
from Tema.views import tema_api_view
from Tema.views import actividadesEnseñanza_api_view
from Tema.views import actividadAprendizaje_api_view
from Tema.views import competenciaGenerica_api_view
from Tema.views import instrumentoEvaluacion_api_view

urlpatterns = [
    path('Tema', tema_api_view, name='tema_api'),
    path('actividadEnseñanza', actividadesEnseñanza_api_view, name='actividadEnseñanza_api'),
    path('actividadAprendizaje', actividadAprendizaje_api_view, name='actividadAprendizaje_api'),
    path('competenciaGenerica', competenciaGenerica_api_view, name='competenciaGenerica_api'),
    path('instrumentoEvaluacion', instrumentoEvaluacion_api_view, name='instrumentoEvaluacion_api')
]
