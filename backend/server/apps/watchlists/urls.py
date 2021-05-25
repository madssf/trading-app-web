from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import WatchlistViewSet

router = DefaultRouter()
router.register("watchlists", WatchlistViewSet, basename="watchlists")
router.register("watchlist_currencies", WatchlistViewSet,
                basename="watchlist_currencies")


watchlists_urlpatterns = [url("api/v1/", include(router.urls))]
