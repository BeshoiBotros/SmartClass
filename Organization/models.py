from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    name          = models.CharField(max_length=255, default='null', blank=False, null=False)
    user          = models.OneToOneField(User, on_delete=models.CASCADE)
    numOfDoctors  = models.IntegerField(default=0, null=False)
    numOfStudents = models.IntegerField(default=0, null=False)
    numOfTAssests = models.IntegerField(default=0, null=False)

    def __str__(self) -> str:
        return self.name
 