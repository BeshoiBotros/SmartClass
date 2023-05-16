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


class TrueOrFalseQ(models.Model):
    quistion = models.TextField(max_length=255)
    answer   = models.BooleanField(null=False)

class MultipleChoiceQ(models.Model):

    answer_choices = [
        ('a', 'a'),
        ('b', 'b'),
        ('c', 'c'),
        ('d', 'd')
    ]

    quistion = models.TextField(max_length=255)
    choiceA  = models.TextField(max_length=255)
    choiceB  = models.TextField(max_length=255)
    choiceC  = models.TextField(max_length=255)
    choiceD  = models.TextField(max_length=255)
    answer   = models.TextField(choices=answer_choices, default='a')
    degree   = models.FloatField(null=False, default=0.0, max_length=5)

class AsSayQ(models.Model):
    pass
