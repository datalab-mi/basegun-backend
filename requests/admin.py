from django.contrib import admin
from .models import Request


class RequestAdmin(admin.ModelAdmin):
    list_display = ["id", "picture", "comment", "status", "updated", "created"]

admin.site.register(Request, RequestAdmin)

