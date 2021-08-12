from datetime import datetime

from django.contrib.sessions.models import Session

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view
from myapps.users.serializers import UserSerializer

class Login(ObtainAuthToken):

    def post(self,request,*args,**kwargs):
        # send to serializer username and password
        login_serializer = self.serializer_class(data = request.data, context = {'request':request})
        if login_serializer.is_valid():
            # login serializer return user in validated_data
            print(login_serializer.validated_data['user'])
        return Response({'message':'AAAAA'}, status = status.HTTP_200_OK)


@api_view(['POST'])
def user_api_view(request):
    
    # create
    if request.method == 'POST':
        user_serializer = UserSerializer(data = request.data)
        
        # validation
        if user_serializer.is_valid():
            user_serializer.save()            
            return Response({'message':'Usuario creado correctamente!'},status = status.HTTP_201_CREATED)
        
        return Response(user_serializer.errors,status = status.HTTP_400_BAD_REQUEST)