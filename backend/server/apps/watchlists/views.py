from rest_framework import viewsets
from .models import Watchlist, WatchlistCurrency
from .serializers import WatchlistSerializer, WatchlistCurrencySerializer
from django.db.models import Q
from apps.users.permissions import OwnerCUD_AuthR


class WatchlistViewSet(viewsets.ModelViewSet):

    serializer_class = WatchlistSerializer
    queryset = Watchlist.objects.all()

    def get_permissions(self):
        return OwnerCUD_AuthR(self, super())

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(Q(owner=self.request.user) | Q(public=True))


class WatchlistCurrencyViewSet(viewsets.ModelViewSet):

    serializer_class = WatchlistCurrencySerializer
    queryset = WatchlistCurrency.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.all()
