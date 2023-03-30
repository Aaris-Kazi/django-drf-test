from django.db import models

# Create your models here.

class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    grade = models.CharField(max_length=50)
    