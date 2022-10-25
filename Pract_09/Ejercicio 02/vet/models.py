from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Mascotas(models.Model):
    nombre = models.CharField(max_length=20)
    propietario = models.CharField(max_length=30)
    especie = models.CharField(max_length=10)
    raza = models.CharField(max_length=15)
