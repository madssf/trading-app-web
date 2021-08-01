from rest_framework import serializers
from .models import Deposit, Portfolio, PortfolioAsset, PortfolioLogEntry, PortfolioParameter, PortfolioPosition, Trade, Credentials


class PortfolioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portfolio
        fields = '__all__'


class PortfolioParameterSerializer(serializers.ModelSerializer):

    class Meta:
        model = PortfolioParameter
        fields = "__all__"


class PortfolioAssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = PortfolioAsset
        fields = '__all__'


class PortfolioPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PortfolioPosition
        field = '__all__'


class PortfolioLogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioLogEntry
        fields = '__all__'


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = '__all__'


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'


class CredentialsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Credentials
        fields = '__all__'