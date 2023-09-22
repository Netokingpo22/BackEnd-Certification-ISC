from django.urls import path
from Clase.views import aula_api_view, grupo_api_view, clase_api_view

urlpatterns = [
    path('Aula', aula_api_view, name='aula_api'),
    path('Grupo', grupo_api_view, name='grupo_api'),
    path('Clase', clase_api_view, name='clase_api'),
]
