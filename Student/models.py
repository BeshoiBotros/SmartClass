from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # role number = 2 point to student
    roleNum = models.IntegerField(default=2)

class Profile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    image   = models.ImageField(upload_to='Student/profiles_images/', default='Student/profiles_images/USER.jpg')

