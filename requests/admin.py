from django.contrib import admin

from .models import Request


class RequestAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Request._meta.get_fields()]


admin.site.register(Request, RequestAdmin)
