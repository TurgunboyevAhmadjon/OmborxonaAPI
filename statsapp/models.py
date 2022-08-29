from django.db import models
from userapp.models import Ombor
from asosiy.models import Client, Mahsulot

class Stats(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, models.SET_NULL, null=True)
    client = models.ForeignKey(Client, models.SET_NULL, null=True)
    sana = models.DateTimeField(auto_now_add=True)
    miqdor = models.PositiveSmallIntegerField()
    umumiy = models.PositiveSmallIntegerField()
    tolandi = models.PositiveSmallIntegerField()
    nasiya = models.PositiveSmallIntegerField()
    ombor = models.ForeignKey(Ombor, models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.mahsulot} {self.client}"



