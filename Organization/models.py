from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Organization(models.Model):
    name          = models.CharField(max_length=255, default='null', blank=False, null=False)
    user          = models.OneToOneField(User, on_delete=models.CASCADE)
    numOfDoctors  = models.IntegerField(default=0, null=False)
    numOfStudents = models.IntegerField(default=0, null=False)
    numOfTAssests = models.IntegerField(default=0, null=False)

    def __str__(self) -> str:
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # role number = 0 point to doctor
    roleNum = models.IntegerField(default=0)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=False, null=False)

class DoctorProfile(models.Model):
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctors/profiles_images/', default='doctors/profiles_images/USER.jpg')

@receiver(post_save, sender = Doctor)
def create_profile(sender, instance, created, **kwargs):
    if created:
        DoctorProfile.objects.create(doctor = instance)