from django.urls import path
from Aula.views import aula_api_view

urlpatterns = [
    path('Aula', aula_api_view, name='aula_api')
]
