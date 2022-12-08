from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from events.models import Event
from profiles.models import Profile
from placements.models import Placement


class Ticket(models.Model):
    owner = models.ForeignKey(Profile, related_name="profiles", on_delete=models.CASCADE, verbose_name="Владелец")
    place = models.ForeignKey(Placement, related_name="events", on_delete=models.CASCADE, verbose_name="Распложение")
    event = models.ForeignKey(Event, related_name="events", on_delete=models.CASCADE, verbose_name="Событие")
    purchase_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата приобретения")
