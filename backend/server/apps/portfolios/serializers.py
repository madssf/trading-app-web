from rest_framework import serializers
from .models import Portfolio, PortfolioParameter


class PortfolioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portfolio
        fields = ['created_at', 'owner', 'name',
                  'strategy', 'description']


class PortfolioParameterSerializer(serializers.ModelSerializer):

    class Meta:
        model = PortfolioParameter
        fields = ['portfolio', 'parameter', 'value']
