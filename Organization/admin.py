from django.contrib import admin
from .models import Organization, DoctorProfile
# Register your models here.

admin.site.register(Organization) 
admin.site.register(DoctorProfile)