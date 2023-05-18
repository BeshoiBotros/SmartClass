from django.shortcuts import render
from SmartClass.permissions import OrganizationPermiaaion
from .serializers import UserSerializer
from Doctor.models import Doctor
from .models import Organization
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

@api_view(['POST'])
# @permission_classes([OrganizationPermiaaion])
def createDoctorView(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    return Response(serializer.data)