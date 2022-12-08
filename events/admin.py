from django.contrib import admin
from .models import Event


@admin.register(Event)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "session_start", "duration_session"]
    list_display_links = ("id", "title")
    search_fields = ("user__username",)

# Register your models here.
