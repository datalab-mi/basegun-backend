from django.contrib import admin

from .models import Analysis, Request


class RequestAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Request._meta.get_fields()]


class AnalysisAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Analysis._meta.get_fields()]
    list_filter = ["label"]


admin.site.register(Request, RequestAdmin)
admin.site.register(Analysis, AnalysisAdmin)
