from rest_framework import viewsets
from .models import Deposit, Portfolio, PortfolioAsset, PortfolioParameter, Trade, Credentials
from .serializers import DepositSerializer, PortfolioAssetSerializer, PortfolioSerializer, PortfolioParameterSerializer, TradeSerializer, CredentialsSerializer


class PortfolioViewSet(viewsets.ModelViewSet):

    serializer_class = PortfolioSerializer
    queryset = Portfolio.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.all()


class PortfolioParameterViewSet(viewsets.ModelViewSet):

    serializer_class = PortfolioParameterSerializer
    queryset = PortfolioParameter.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.all()


class PortfolioAssetView(viewsets.ModelViewSet):

    serializer_class = PortfolioAssetSerializer
    queryset = PortfolioAsset.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.all()


class TradeViewSet(viewsets.ModelViewSet):

    serializer_class = TradeSerializer
    queryset = Trade.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.all()


class DepositViewSet(viewsets.ModelViewSet):

    serializer_class = DepositSerializer
    queryset = Deposit.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.all()


class CredentialsViewSet(viewsets.ModelViewSet):

    serializer_class = CredentialsSerializer
    queryset = Credentials.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
