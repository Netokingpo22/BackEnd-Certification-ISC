from django.urls import path
from Usuario.views import usuario_api_view

urlpatterns = [
    path('Usuario', usuario_api_view, name='usuario_api')
]
