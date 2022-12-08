from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (("male", "Male"), ("female", "Female"))

class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    date_of_birth = models.DateField(
        blank=True, null=True, verbose_name="Дата рождения"
    )
    gender = models.CharField(
        max_length=25, choices=GENDER_CHOICES, blank=True, null=True, verbose_name="Пол"
    )

    def __str__(self):
        return f"Профиль пользователя: {self.user}"
# Create your models here.
