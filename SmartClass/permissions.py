from rest_framework.permissions import BasePermission
from Organization.models import Organization, Doctor

class OrganizationPermission(BasePermission):

    def has_permission(self, request, view):
        try:
            org = Organization.objects.get(user = request.user.id)
            return True
        except Organization.DoesNotExist:
            return False
    
    def has_object_permission(self, request, view, obj):
        
        try:
            org = Organization.objects.get(user=request.user)
            if obj.user == org.user:
                return True
            return False
        except Organization.DoesNotExist:
            return False
        

class DoctorPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            doc = Doctor.objects.get(user = request.user.id)
            if obj.user == doc.user:
                return True
            return False
        except Doctor.DoesNotExist:
            return False
    def has_permission(self, request, view):
        try:
            doc = Doctor.objects.get(user = request.user.id)
            return True
        except Doctor.DoesNotExist:
            return False