from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isDoctor = models.BooleanField(default=True)

class Material(models.Model):
    name = models.TextField(max_length=255)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

class Research(models.Model):
    content = models.TextField(blank=False, null=False)
    Date = models.DateField(null=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

class Certificate(models.Model):
    name = models.TextField(max_length=255)
    description = models.TextField(null=False, blank=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctors/certificates/', default='doctors/certificates/DC.jpg')

class Profile(models.Model):
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctors/profiles_images/', default='doctors/profiles_images/USER.jpg')
    

