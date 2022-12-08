from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ["id", "owner", "event", "place"]
    list_display_links = ("id", "owner", "event", "place")
    search_fields = ("user__username",)

# Register your models here.
