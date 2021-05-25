from rest_framework import serializers
from .models import Watchlist, WatchlistCurrency


class WatchlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Watchlist
        fields = ['created_at', 'owner', 'name',
                  'description']


class WatchlistCurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchlistCurrency
        fields = ['added_at', 'watchlist', 'currency', 'note']
