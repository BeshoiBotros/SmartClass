from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    user          = models.OneToOneField(User, on_delete=models.CASCADE)
    numOfDoctors  = models.IntegerField(default=0, null=False)
    numOfStudents = models.IntegerField(default=0, null=False)
    numOfTAssests = models.IntegerField(default=0, null=False)
