from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
#serialisers
from .serializer import RegistrationSerializer
# Create your views here.

@api_view(['POST'])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    data ={}
    if serializer.is_valid():
        account = serializer.save()
        data['resposnse']="Sucessfully Registered User"+"  with email  " +account.email
        data['Token'] = Token.objects.get(user = account).key

    else:
        data = serializer.errors
    return Response(data)    
