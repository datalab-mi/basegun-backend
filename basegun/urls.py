from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from weapons.views import AnalysisViewSet, RequestViewSet

router = DefaultRouter()
router.register(r"requests", RequestViewSet, basename="requests")
router.register(r"analyses", AnalysisViewSet, basename="analyses")

urlpatterns = (
    router.urls
    + [
        path("api/", include(router.urls)),
        path("admin/", admin.site.urls),
        path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
        path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
