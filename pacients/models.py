from django.db import models

# Create your models here.

# class Diagnostic(models.Model):
#     diag = models.CharField(max_length=30)


class Pacient(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    dni = models.IntegerField()
    # diagnosis = models.ForeignKey(Diagnostic, on_delete=models.PROTECT)
