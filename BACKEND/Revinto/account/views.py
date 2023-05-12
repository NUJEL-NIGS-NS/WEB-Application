from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
#models
from .models import Account
#serialisers
from .serializer import RegistrationSerializer
# Create your views here.

@api_view(['POST'])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    data ={}
    if serializer.is_valid():
        account = serializer.save()
        data['status']="Sucessfully Registered User"+"  with email  " +account.email
        data['token'] = Token.objects.get(user = account).key

    else:
        data = serializer.errors
    return Response(data)    

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_token(request):
    data={}
    try:
        user = Token.objects.get(user=request.user)
        user.delete()
        data['status']=True
    except:
        data['status']=False
    return Response(data)    

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_details(request):
    user = request.user
    data ={}
    try:
        data['name']=user.username
        data['designation']=user.designation

    except:
        data['name']='error'
    return Response(data)         

   
