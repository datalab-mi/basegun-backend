from rest_framework import serializers

from .models import Request


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = [field.name for field in Request._meta.get_fields()]
