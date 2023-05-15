from django.db import models


class Video(models.Model):
    title = models.TextField(max_length=255)
    # complate the model
    video = models.FileField(upload_to='')