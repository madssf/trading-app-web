from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import ExchangeViewSet, CredentialsViewSet

router = DefaultRouter()
router.register("exchanges", ExchangeViewSet, basename="exchanges")
router.register("credentials", CredentialsViewSet, basename="credentials")

exchanges_urlpatterns = [url("api/v1/", include(router.urls))]
