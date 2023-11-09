from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .usuarioSerializers import userSerializers

from django.shortcuts import get_object_or_404

# Create your views here.


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "not found"}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serialaizer = userSerializers(instance=user)
    return Response({"token": token.key, "id": serialaizer.data['id'], "username": serialaizer.data['username']})


@api_view(['POST'])
def singup(request):
    serializer = userSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
