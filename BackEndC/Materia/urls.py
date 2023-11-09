from django.urls import path
from Materia.views import materia_api_view, intencionDidactica_api_view

urlpatterns = [
    path('Materia', materia_api_view, name='materia_api'),
    path('intencion_Didactica', intencionDidactica_api_view,
         name='intencionDidactica_api')
]
