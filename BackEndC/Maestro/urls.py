from django.urls import path
from Maestro.views import maestro_api_view

urlpatterns = [
    path('Maestro', maestro_api_view, name='maestro_api')
]
