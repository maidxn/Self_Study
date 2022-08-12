from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=50)
    quirk = models.CharField(max_length=50)