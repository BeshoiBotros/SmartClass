from django.db import models
from django.contrib.auth.models import User
from Doctor.models import Doctor

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isStudent = models.BooleanField(default=True)

class Profile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    image   = models.ImageField(upload_to='Student/profiles_images/', default='Student/profiles_images/USER.jpg')

class PaidCourses(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    # subject here after createing subject model