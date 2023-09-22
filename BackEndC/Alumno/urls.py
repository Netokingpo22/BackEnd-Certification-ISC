from django.urls import path
from Alumno.views import alumno_api_view

urlpatterns = [
    path('Alumno', alumno_api_view, name='alumno_api')
]
