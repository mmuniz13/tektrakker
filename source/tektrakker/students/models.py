from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)