from django.db import models
from Doctor.models import Doctor
from T_assest.models import TAssest
from Student.models import Student

class Subject(models.Model):
    name = models.CharField(max_length=255)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=False)
    price = models.FloatField(max_length=5, default=0.0)
    pdf = models.FileField(upload_to='subjects/pdfs/', null=True)

class Chapter(models.Model):
    title = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=False)

class Video(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='subjects/videos/', null=False)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=False)
    description = models.TextField(null=True, blank=True)


class TrueOrFalseQ(models.Model):
    level_choices = [
        ('easy','easy'),
        ('medium', 'medium'),
        ('hard','hard')
    ]
    quistion = models.CharField(max_length=255)
    answer   = models.BooleanField(null=False)
    degree   = models.FloatField(null=False, default=0.0, max_length=5)
    level    = models.CharField(choices=level_choices, max_length=255, default='easy')
    subject  = models.ForeignKey(Subject, on_delete=models.CASCADE)
    tAssest  = models.ForeignKey(TAssest, on_delete=models.PROTECT)
    
class   (models.Model):

    answer_choices = [
        ('a', 'a'),
        ('b', 'b'),
        ('c', 'c'),
        ('d', 'd')
    ]

    level_choices = [
        ('easy','easy'),
        ('medium', 'medium'),
        ('hard','hard') 
    ]
    
    quistion = models.TextField(max_length=255)
    choiceA  = models.CharField(max_length=255)
    choiceB  = models.CharField(max_length=255)
    choiceC  = models.CharField(max_length=255)
    choiceD  = models.CharField(max_length=255)
    answer   = models.CharField(choices=answer_choices, default='a', max_length=255)
    degree   = models.FloatField(null=False, default=0.0, max_length=5)
    level    = models.CharField(choices=level_choices, max_length=255, default='easy')
    subject  = models.ForeignKey(Subject, on_delete=models.CASCADE)
    tAssest  = models.ForeignKey(TAssest, on_delete=models.PROTECT)


class AsSayQ(models.Model):
    pass


class QuestionsBank(models.Model):
    subject         = models.ForeignKey(Subject, on_delete=models.CASCADE)
    multipleChoiceQ = models.ManyToManyField('MultipleChoiceQ')
    trueOrFalseQ    = models.ManyToManyField('TrueOrFalseQ', blank=True)

class Quiz(models.Model):
    subject         = models.ForeignKey(Subject, on_delete=models.CASCADE)
    multipleChoiceQ = models.ManyToManyField('MultipleChoiceQ')
    trueOrFalseQ    = models.ManyToManyField('TrueOrFalseQ', blank=True)
    startDate       = models.DateTimeField(auto_now_add=True)
    endDate         = models.DateTimeField(null=False)

class Assignment(models.Model):
    subject         = models.ForeignKey(Subject, on_delete=models.CASCADE)
    multipleChoiceQ = models.ManyToManyField('MultipleChoiceQ')
    trueOrFalseQ    = models.ManyToManyField('TrueOrFalseQ', blank=True)
    startDate       = models.DateTimeField(auto_now_add=True)
    endDate         = models.DateTimeField(null=False)

class QuizsDegree(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    degree  = models.FloatField(max_length=5, default=0.0)
    quiz    = models.ForeignKey(Quiz, on_delete=models.PROTECT)
