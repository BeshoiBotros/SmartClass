from django.shortcuts import render
from SmartClass.permissions import OrganizationPermission
from .serializers import UserSerializer, DoctorSerializer
from Doctor.models import Doctor, Profile
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
        org = Organization.objects.get(user = request.user)
    except:
        msg = "Authentication credentials were not provided."
        return Response({'msg' : msg}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    docsOfOrg = Doctor.objects.all().filter(organization = org).count()
    if org.numOfDoctors > docsOfOrg:
        try:
            user = serializer.create(request.data)
        except:
            msg = "User already exist try again"
            return Response({'msg' : msg}, status=status.HTTP_400_BAD_REQUEST)
    
        try:
            doctor = Doctor.objects.create(user = User.objects.get(username = user.username), organization=org)
            doctorProfile = Profile.objects.create(doctor = doctor)
        except:
            msg = "something goes wrong!"
    else:
        msg = "the number of doctor has reached the maximum number"
        return Response({'msg' : msg}, status=status.HTTP_501_NOT_IMPLEMENTED)

    msg = "Doctor created successfuly"
    return Response({'msg' : msg}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([OrganizationPermission])
def viewDoctors(request):
    try:
        org = Organization.objects.get(user = request.user)
    except:
        msg = "Authentication credentials were not provided."
        return Response({'msg' : msg}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    doctorsOfOrg = Doctor.objects.all().filter(organization=org)
    serializer = DoctorSerializer(doctorsOfOrg, many=True)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    