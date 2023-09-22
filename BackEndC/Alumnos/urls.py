from django.urls import path
from Alumnos.views import alumnos_api_view

urlpatterns = [
    path('Alumnos', alumnos_api_view, name='alumnos_api')
]
