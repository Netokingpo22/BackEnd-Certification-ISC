from django.urls import path
from IntencionDidactica.views import intencionDidactica_api_view

urlpatterns = [
    path('intencion_Didactica', intencionDidactica_api_view, name='intencionDidactica_api')
]
