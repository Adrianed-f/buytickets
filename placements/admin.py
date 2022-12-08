from django.contrib import admin
from .models import Placement


@admin.register(Placement)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "row", "seat"]
    list_display_links = ("id", "row", "seat")
    search_fields = ("user__username",)
# Register your models here.
