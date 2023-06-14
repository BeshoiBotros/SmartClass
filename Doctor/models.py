from django.db import models
from django.contrib.auth.models import User
from Organization.models import Doctor

    

class Material(models.Model):
    name = models.CharField(max_length=255)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

class Research(models.Model):
    content = models.TextField(blank=False, null=False)
    Date = models.DateField(null=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

class Certificate(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=False, blank=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctors/certificates/', default='doctors/certificates/DC.jpg')


    
