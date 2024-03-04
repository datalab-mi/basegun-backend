import os
from uuid import uuid4

from rest_framework import mixins, viewsets

from .apps import WeaponsConfig
from .models import Analysis, Request
from .serializers import AnalysisSerializer, RequestSerializer
from .utils.model import predict_image


class RequestViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class AnalysisViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer

    def perform_create(self, serializer):
        picture_bytes = serializer.validated_data["picture"].file.read()
        label, confidence = predict_image(WeaponsConfig.ML_MODEL, picture_bytes)
        serializer.save(label=label, confidence=confidence)
