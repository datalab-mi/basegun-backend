from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from .models import Analysis, Request


class RequestSerializer(serializers.ModelSerializer):
    picture_left = Base64ImageField()
    picture_right = Base64ImageField()
    picture_markings = Base64ImageField()
    picture_charger = Base64ImageField()

    class Meta:
        model = Request
        fields = [field.name for field in Request._meta.get_fields()]


class AnalysisSerializer(serializers.ModelSerializer):
    picture = Base64ImageField()

    class Meta:
        model = Analysis
        fields = ["picture"]

    def to_representation(self, instance):
        if instance.confidence < 0.76:
            confidence_level = "low"
        elif instance.confidence < 0.98:
            confidence_level = "medium"
        else:
            confidence_level = "high"
        return {
            "picture": instance.picture.url,
            "label": instance.label,
            "confidence": instance.confidence,
            "confidence_level": confidence_level,
        }
