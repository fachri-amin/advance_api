from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from account.api.serializers import AccountSerializers
from rest_framework.authtoken.models import Token


@api_view(['POST', ])
def api_registration_view(request):

    if request.method == 'POST':
        serializers = AccountSerializers(data=request.data)
        if serializers.is_valid():
            account = serializers.save()
            token = Token.objects.get(user=account).key
            data = {
                'response': 'successfully registered new user',
                'email': account.email,
                'username': account.username,
                'token': token,
            }
        else:
            data = serializers_data.errors
        return Response(data)
