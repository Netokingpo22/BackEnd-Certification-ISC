from django.urls import path

from Alumno.views import alumno_api_view
from Alumno.views import alumnoClase_api_view
from Alumno.views import alumnoTemaClase_api_view

urlpatterns = [
    path('Alumno', alumno_api_view, name='alumno_api'),
    path('AlumnoClase', alumnoClase_api_view, name='alumnoClase_api'),
    path('AlumnoTemaClase', alumnoTemaClase_api_view, name='alumnoTemaClase_api')
]
