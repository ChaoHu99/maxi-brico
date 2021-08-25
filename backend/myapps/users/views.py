from datetime import datetime

from django.contrib.sessions.models import Session

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view
from myapps.users.serializers import UserSerializer
from myapps.users.serializers import UserTokenSerializer
from rest_framework.permissions import AllowAny


@api_view(['GET'])
def get_current_user(request):
    
    if request.method == 'GET':
        user = request.user
        return Response({'user': user.id}, status = status.HTTP_200_OK)

    else:
        return Response({'message':'The request must be a GET'}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_api_view(request):
    permission_classes = (AllowAny,)

    if request.method == 'POST':
        user_serializer = UserSerializer(data = request.data)
        
        # validation
        if user_serializer.is_valid():
            user_serializer.save()            
            return Response({'message':'User created successfully!'},status = status.HTTP_201_CREATED)
        
        return Response(user_serializer.errors,status = status.HTTP_400_BAD_REQUEST)