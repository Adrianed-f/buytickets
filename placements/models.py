from django.conf import settings
from django.db import models


class Placement(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()

