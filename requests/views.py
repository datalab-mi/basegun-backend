from rest_framework import mixins, viewsets

from .models import Request
from .serializers import RequestSerializer


class RequestViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
