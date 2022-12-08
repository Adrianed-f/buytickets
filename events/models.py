from django.conf import settings
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название События")
    about = models.TextField(verbose_name="О событии")
    session_start = models.DateTimeField(verbose_name="Начало сеанса")
    duration_session = models.CharField(max_length=8,verbose_name="Продолжительность сеанса")

    def __str__(self):
        return self.title

# Create your models here.