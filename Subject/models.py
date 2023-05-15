from django.db import models
from Doctor.models import Doctor


class Subject(models.Model):
    name = models.TextField(max_length=255)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=False)
    price = models.FloatField(max_length=5, default=0.0)
    pdf = models.FileField(upload_to='subjects/pdfs/', null=True)

class Chapter(models.Model):
    title = models.TextField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=False)

class Video(models.Model):
    title = models.TextField(max_length=255)
    video = models.FileField(upload_to='subjects/videos/', null=False)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=False)

