from django.contrib import admin
from tips.models import Message
# Register your models here.

class MessageFilter(admin.ModelAdmin):
    list_display = ["title", "event_date", "location"]
    list_filter = ["title", "event_date"]
    search_fields = ["title", "location"]

admin.site.register(Message, MessageFilter)