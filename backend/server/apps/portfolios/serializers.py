from rest_framework import serializers
from .models import Deposit, Portfolio, PortfolioAsset, PortfolioParameter, Trade, Credentials


class PortfolioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portfolio
        fields = ['id', 'created_at', 'owner', 'name',
                  'strategy', 'description', 'public']


class PortfolioParameterSerializer(serializers.ModelSerializer):

    class Meta:
        model = PortfolioParameter
        fields = ['portfolio', 'parameter', 'value']


class PortfolioAssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = PortfolioAsset
        fields = ['id', 'portfolio', 'currency', 'timestamp', 'exchange', 'locked', 'flex', 'spot',
                  'average', 'flex_apr', 'flex_start', 'locked_apr', 'locked_start', 'locked_end']


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ['portfolio', 'exchange', 'buy_currency',
                  'sell_currency', 'buy_amount', 'sell_amount', 'timestamp']


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ['portfolio', 'currency', 'amount', 'timestamp']


class CredentialsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Credentials
        fields = ['created_at', 'owner', 'exchange',
                  'portfolio', 'api_key', 'api_secret', 'api_payload']
