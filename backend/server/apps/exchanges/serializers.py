from rest_framework import serializers
from .models import Exchange


class ExchangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exchange
        fields = ['added_at', 'added_by', 'name',
                  'description', 'web_url', 'api_url']
