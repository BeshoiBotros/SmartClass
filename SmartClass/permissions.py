from rest_framework.permissions import BasePermission
from Organization.models import Organization

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
        
