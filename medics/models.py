from django.db import models

# Create your models here.

class Medic(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    medic_type = models.CharField(max_length=20)