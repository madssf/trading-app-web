from rest_framework import viewsets
from .models import Watchlist, WatchlistCurrency
from .serializers import WatchlistSerializer, WatchlistCurrencySerializer


class WatchlistViewSet(viewsets.ModelViewSet):

    serializer_class = WatchlistSerializer
    queryset = Watchlist.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return self.queryset.all()


class WatchlistCurrencyViewSet(viewsets.ModelViewSet):

    serializer_class = WatchlistCurrencySerializer
    queryset = WatchlistCurrency.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.all()
