from django.db import models

# Create your models here.
class ToDo(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    status=models.CharField(max_length=50)