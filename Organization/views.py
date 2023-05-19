from django.shortcuts import render
from SmartClass.permissions import OrganizationPermission
from .serializers import UserSerializer
from Doctor.models import Doctor
from .models import Organization
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
@permission_classes([OrganizationPermission])
def createDoctorView(request):
    msg = ""
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    try:
        user = serializer.create(request.data)
    except:
        msg = "User already exist try again"
        return Response({'msg' : msg}, status=status.HTTP_400_BAD_REQUEST)
    try:
        org = Organization.objects.get(user = request.user)
    except:
        msg = "Authentication credentials were not provided."
        return Response({'msg' : msg}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    try:
        doctor = Doctor.objects.create(user = User.objects.get(username = user.username), organization=org)
    except:
        msg = "something goes wrong!"
    msg = "Doctor created successfuly"
    return Response({'msg' : msg}, status=status.HTTP_201_CREATED)