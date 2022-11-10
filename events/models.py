from django.conf import settings
from django.db import models
from placements.models import Placement


class Event(models.Model):
    title = models.CharField(max_length=200)
    place = models.ForeignKey(Placement, related_name="events", on_delete=models.CASCADE)
    session_start = models.DateTimeField()
    session_end = models.DateTimeField()

# Create your models here.