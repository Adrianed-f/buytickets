from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from events.models import Event


class Ticket(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tickets",
        blank=True,
        null=True,
    )

    event = models.ForeignKey(Event, related_name="events", on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True, db_index=True)
