from django.urls import path
from AtributoEgreso.views import atributoEgreso_api_view, criterioDesempeño_api_view, indicador_api_view

urlpatterns = [
    path('AtributoEgreso', atributoEgreso_api_view, name='atributoEgreso_api'),
    path('CriterioDesempeño', criterioDesempeño_api_view, name='criterioDesempeño_api'),
    path('Indicador', indicador_api_view, name='indicador_api'),
]
