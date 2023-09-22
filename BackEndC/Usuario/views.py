from rest_framework.response import Response
from rest_framework.decorators import api_view
from Usuario.usuarioSerializers import userSerializers

from Usuario.models import Usuario

# Create your views here.


@api_view(['GET', 'POST'])
def usuario_api_view(request):

    if request.method == 'GET':
        usuraio = Usuario.objects.all()
        usuraiosSerializer = userSerializers(usuraio, many=True)
        return Response(usuraiosSerializer.data)
    
    elif request.method == 'POST':
        usuraiosSerializer = userSerializers(data=request.data)
        if usuraiosSerializer.is_valid():
            usuraiosSerializer.save()
            return Response(usuraiosSerializer.data)
        return Response(usuraiosSerializer.errors)