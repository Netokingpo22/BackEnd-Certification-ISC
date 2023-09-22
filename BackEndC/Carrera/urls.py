from django.urls import path
from Carrera.views import carrera_api_view

urlpatterns = [
    path('Carrera', carrera_api_view, name='carerra_api')
]
