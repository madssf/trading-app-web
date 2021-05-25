from rest_framework import serializers
from .models import Credentials, Exchange


class ExchangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exchange
        fields = ['added_at', 'added_by', 'name',
                  'description', 'web_url', 'api_url']


class CredentialsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Credentials
        fields = ['created_at', 'owner', 'exchange',
                  'portfolio', 'api_key', 'api_secret', 'api_payload']
