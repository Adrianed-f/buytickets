from django.conf import settings
from django.db import models

ROW_CHOICES = {
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
}
SEAT_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
)

class Placement(models.Model):
    row = models.IntegerField(choices= ROW_CHOICES, verbose_name="Ряд")
    seat = models.IntegerField(choices= SEAT_CHOICES,verbose_name="Место")

    def __str__(self):
        return f"{self.row} ряд {self.seat} место"

