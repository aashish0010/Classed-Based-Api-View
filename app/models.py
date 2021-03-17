from django.db import models

# Create your models here.

class Home(models.Model):
    username = models.CharField(max_length=220)
    email = models.EmailField()
    password = models.CharField(max_length=220)