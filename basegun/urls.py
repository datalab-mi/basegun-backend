from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from requests.views import RequestViewSet

router = DefaultRouter()
router.register(r"requests", RequestViewSet, basename="requests")

urlpatterns = (
    router.urls
    + [
        path("api/", include(router.urls)),
        path("admin/", admin.site.urls),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
