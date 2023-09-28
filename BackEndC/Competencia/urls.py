from django.urls import path

from Competencia.views import competencia_api_view
from Competencia.views import listaCompetencia_api_view

urlpatterns = [
    path('Competencia', competencia_api_view, name='competencia_api'),
    path('listaCompetencia', listaCompetencia_api_view, name='listaCompetencia_api'),
]
