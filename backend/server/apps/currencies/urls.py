from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import CurrencyAndStatView, CurrencyStatViewSet, CurrencyTagViewSet, CurrencyViewSet, MCAPTotalViewSet, TagGroupViewSet, TagViewSet
from django.urls import path

router = DefaultRouter()
router.register("currencies", CurrencyViewSet, basename="currencies")
router.register("tag_groups", TagGroupViewSet, basename="tag_groups")
router.register("tags", TagViewSet, basename="tag")
router.register("currency_tags", CurrencyTagViewSet, basename="currency_tags")
router.register("mcap_total", MCAPTotalViewSet,
                basename="mcap_total")
router.register("currency_stats", CurrencyStatViewSet,
                basename="currency_stats")


bot_currencies = [path(
    "api/v1/bot/currencies", CurrencyAndStatView.as_view(), name='bot-currencies')]
currencies_urlpatterns = [
    url("api/v1/", include(router.urls))] + bot_currencies
