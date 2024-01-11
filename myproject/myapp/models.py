from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(max_length=255)
    father_name = models.CharField(max_length=255)