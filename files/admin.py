from django.contrib import admin

from .models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ("pk", "upload_at", "processed")
    list_filter = ("upload_at", "processed")
