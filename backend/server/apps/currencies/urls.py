from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import CurrencyTagViewSet, MCAPTotalViewSet, TagGroupViewSet, TagViewSet, CurrencyCreateView, CurrencyDetailView, CurrencyUpdateView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


router = DefaultRouter()
#router.register("currencies", CurrencyViewSet, basename="currencies")
router.register("tag_groups", TagGroupViewSet, basename="tag_groups")
router.register("tags", TagViewSet, basename="tag")
router.register("currency_tags", CurrencyTagViewSet, basename="currency_tags")
router.register("mcap_total", MCAPTotalViewSet,
                basename="mcap_total")

currencies = [

    path(route='api/v1/currencies/<slug:slug>/edit/',
         view=csrf_exempt(CurrencyUpdateView.as_view()),
         name='update',
         ),
    path(route='api/v1/currencies/<slug:slug>/',
         view=csrf_exempt(CurrencyDetailView.as_view()),
         name='detail',
         ),
    path(route='api/v1/currencies/',
         view=csrf_exempt(CurrencyCreateView.as_view()),
         name='create',
         )

]


currencies_urlpatterns = [
    url("api/v1/", include(router.urls))] + currencies
