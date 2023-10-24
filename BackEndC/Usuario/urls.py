from django.urls import path
from Usuario.views import singup, login

urlpatterns = [
    path('singup', singup, name='usuario_api'),
    path('login', login, name='usuario_api')
]
