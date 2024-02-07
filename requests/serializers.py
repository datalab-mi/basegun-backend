from rest_framework import serializers

from .models import Analysis, Request


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = [field.name for field in Request._meta.get_fields()]


class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = ["picture"]

    def to_representation(self, instance):
        return {
            "picture": instance.picture.url,
            "label": instance.label,
            "confidence": instance.confidence,
        }
