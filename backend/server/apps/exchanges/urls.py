from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import ExchangeViewSet

router = DefaultRouter()
router.register("exchanges", ExchangeViewSet, basename="exchanges")

exchanges_urlpatterns = [url("api/v1/", include(router.urls))]
