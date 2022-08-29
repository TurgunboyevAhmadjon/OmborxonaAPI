from django.contrib.auth.models import User
from django.db import models


class Ombor(models.Model):
    ism = models.CharField(max_length=30)
    nom = models.CharField(max_length=100)
    telefon = models.CharField(max_length=15)
    manzil = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.ism} ({self.nom})"

