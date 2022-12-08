from django.contrib.auth.models import User
from django.core.management import BaseCommand

from placements.models import Placement, ROW_CHOICES, SEAT_CHOICES

from random import randint


class Command(BaseCommand):
    help = "generate placements"

    def handle(self, *args, **options):
        i = 1
        j = 1

        while j <= 10:
            Placement.objects.create(row = i, seat = j)
            j += 1
            if j == 11:
                i += 1
                j = 1
                if i == 11:
                    break