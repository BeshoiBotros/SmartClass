from django.db import models
from django.contrib.auth.models import User
from Doctor.models import Doctor


class TAssest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # role number = 1 point to teacher assest
    roleNum = models.IntegerField(default=1)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

class Profile(models.Model):
    tAssest = models.OneToOneField(TAssest, on_delete=models.CASCADE)
    image   = models.ImageField(upload_to='T-assest/profiles_images/', default='T-assest/profiles_images/USER.jpg')