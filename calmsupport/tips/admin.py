from django.contrib import admin
from tips.models import Uploads
# Register your models here.

class UploadFilter(admin.ModelAdmin):
    list_display = ["title", "event_date", "location"]
    list_filter = ["title", "event_date"]
    search_fields = ["title", "location"]

admin.site.register(Uploads, UploadFilter)