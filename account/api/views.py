from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from account.api.serializers import AccountSerializers, AccountPropertiesSerializer, ChangeAccountPasswordSerializer
from rest_framework.authtoken.models import Token
from account.models import Account


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


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def account_properties_view(request):
    try:
        account = request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AccountPropertiesSerializer(account)

    return Response(serializer.data)


@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def account_update_view(request):
    try:
        account = request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AccountPropertiesSerializer(account, request.data)
    if serializer.is_valid():
        serializer.save()
        data = {
            'response': 'Update account success'
        }
        return Response(data=data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def change_password_view(request):
    account = request.user
    serializer = ChangeAccountPasswordSerializer(account, data=request.data)
    # print(account.check_password())
    if request.data.get('new_password') != request.data.get('new_password2'):
        data = {
            'response': 'Password must be match!',
        }
        return Response(data=data)

    if serializer.is_valid():
        # Check old password
        if not account.check_password(request.data.get("old_password")):
            return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
        # set_password also hashes the password that the user will get
        account.set_password(request.data.get("new_password"))
        serializer.save()
        response = {
            'status': 'success',
            'code': status.HTTP_200_OK,
            'message': 'Password updated successfully',
            'data': []
        }

        return Response(response)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
