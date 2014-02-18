import os
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=256)

class Media(models.Model):
    course = models.ForeignKey(Course, null=True)
    file = models.FileField(upload_to = 'media')
    