from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MasterStates

# Create your views here.
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def state_list_view(request):
    data=[]
    try:
        queryset = MasterStates.objects.values('State','Path').distinct()
        for i in queryset:
            set1={}
            set1['State']=i['State']
            set1['Path']=i['Path']
            data.append(set1)
    except Exception as e:
        print(e)
        data=[]
    return Response(data)            