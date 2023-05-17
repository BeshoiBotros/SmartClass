from django.contrib import admin
from .models import *


admin.site.register(Subject)
admin.site.register(Chapter)
admin.site.register(Video)
admin.site.register(TrueOrFalseQ)
admin.site.register(MultipleChoiceQ)
admin.site.register(QuestionsBank)
admin.site.register(Quiz)
admin.site.register(Assignment)
admin.site.register(QuizsDegree)