from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from auth_token.api.serializers import TokenSerializer
from django.contrib.auth import authenticate

from rest_framework.authtoken.models import Token
from account.models import Account

@api_view(['POST',])
@permission_classes(())
def api_token_retrieval_view(request):
    
    data = request.data
    if 'email' in data.keys() and 'password' in data.keys():
        email = data['email']
        password = data['password']
        try:
            user = Account.objects.get(email=email)
        except:
            content = {
                "status": "Wrong Credentials!"
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND) 
    else:
        content = {
                "status": "No Credentials Were Provided!"
            }
        return Response(content, status=status.HTTP_404_NOT_FOUND)  

    check = authenticate(username=email, password=password)
    if check is not None:
        queryset = Token.objects.filter(user=user)
        token = queryset[0]

        serializer = TokenSerializer(token)
        return Response(serializer.data)
    else:
        response = {
            "status": "Wrong Credentials!"
        }
        return Response(response, status=status.HTTP_404_NOT_FOUND) 

    
