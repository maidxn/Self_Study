from pyexpat import model
from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=100)
    hero_name = models.CharField(max_length=500)
    quirk = models.CharField(max_length=100)
    dob = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

