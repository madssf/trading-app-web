from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import CurrencyBatchView, CurrencyTagViewSet, MCAPTotalViewSet, TagGroupViewSet, TagViewSet, CurrencyViewSet
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


router = DefaultRouter()
router.register("currencies", CurrencyViewSet, basename="currencies")
router.register("tag_groups", TagGroupViewSet, basename="tag_groups")
router.register("tags", TagViewSet, basename="tag")
router.register("currency_tags", CurrencyTagViewSet, basename="currency_tags")
router.register("mcap_total", MCAPTotalViewSet,
                basename="mcap_total")

batch_update_url = [path(
    "api/v1/bot/currency_batch_update", csrf_exempt
    (CurrencyBatchView.as_view()), name='currencies_batch_update')]

currencies_urlpatterns = [
    url("api/v1/", include(router.urls))] + batch_update_url
