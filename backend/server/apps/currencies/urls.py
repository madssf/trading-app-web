from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import CurrencyTagViewSet, CurrencyViewSet, TagGroupViewSet, TagViewSet

router = DefaultRouter()
router.register("currencies", CurrencyViewSet, basename="currencies")
router.register("tag_groups", TagGroupViewSet, basename="tag_groups")
router.register("tags", TagViewSet, basename="tag")
router.register("currency_tags", CurrencyTagViewSet, basename="currency_tags")

currencies_urlpatterns = [url("api/v1/", include(router.urls))]
