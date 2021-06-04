from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import CurrencyTagViewSet, CurrencyViewSet, MCAPTotalViewSet, TagGroupViewSet, TagViewSet

router = DefaultRouter()
router.register("currencies", CurrencyViewSet, basename="currencies")
router.register("tag_groups", TagGroupViewSet, basename="tag_groups")
router.register("tags", TagViewSet, basename="tag")
router.register("currency_tags", CurrencyTagViewSet, basename="currency_tags")
router.register("mcap_total", MCAPTotalViewSet,
                basename="mcap_total")


currencies_urlpatterns = [
    url("api/v1/", include(router.urls))]
