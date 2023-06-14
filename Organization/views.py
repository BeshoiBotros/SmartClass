from rest_framework import generics
from SmartClass.permissions import OrganizationPermission
from .serializers import CreateDoctorSerializer, DoctorSerializer, DeleteDoctorSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import Organization
from .models import Doctor
from rest_framework import serializers
from rest_framework.decorators import permission_classes, api_view
from django.contrib.auth.models import User

class CreateDoctorView(generics.CreateAPIView):
    permission_classes = [OrganizationPermission]
    serializer_class = CreateDoctorSerializer
    queryset = Doctor.objects.all()
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request' : self.request})
        return context

    def perform_create(self, serializer):
        try:
            org = Organization.objects.get(user = self.request.user)
        except:
            return Response("the user is not an Organization.", status=status.HTTP_400_BAD_REQUEST)
        doctors = Doctor.objects.filter(organization = org).count()
        print(doctors < org.numOfDoctors)
        if doctors >= org.numOfDoctors:
            raise serializers.ValidationError({"msg":"The doctors in your organization have reached the maximum number. Please upgrade to add more :)"})
        serializer.save()

class ViewDoctorsView(generics.ListAPIView):
    permission_classes = [OrganizationPermission]
    serializer_class   = DoctorSerializer
    def get_queryset(self):
        return Doctor.objects.filter(organization = Organization.objects.get(user = self.request.user))
    
class DeleteDoctor(generics.DestroyAPIView):
    serializer_class = DeleteDoctorSerializer
    permission_classes = [OrganizationPermission]
    queryset = Doctor.objects.all()
    def get_queryset(self):
        organization = self.request.user.organization
        return super().get_queryset().filter(organization=organization)

@api_view(['DELETE'])
@permission_classes([OrganizationPermission])
def deleteDoctor(request, pk):
    organization = Organization.objects.get(user = request.user)
    doctor = Doctor.objects.get(id = pk)
    if doctor.organization != organization:
        return Response({'detail' : 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    User.objects.get(pk  = doctor.user.pk).delete()
    doctor.delete()
    return Response({'msg' : "doctor deleted successfuly"})