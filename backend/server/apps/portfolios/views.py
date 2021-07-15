from django.contrib.auth import get_user_model
from rest_framework import viewsets
from apps.users.permissions import OwnerCUD_AuthR, IsOwner
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response

from .models import Deposit, Portfolio, PortfolioAsset, PortfolioLogEntry, PortfolioParameter, PortfolioPosition, Trade, Credentials
from .serializers import DepositSerializer, PortfolioAssetSerializer, PortfolioLogEntrySerializer, PortfolioPositionSerializer, PortfolioSerializer, PortfolioParameterSerializer, TradeSerializer, CredentialsSerializer


User = get_user_model()


class PortfolioViewSet(viewsets.ModelViewSet):

    permission_classes = [IsOwner]
    serializer_class = PortfolioSerializer
    queryset = Portfolio.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class PortfolioParameterViewSet(viewsets.ModelViewSet):

    serializer_class = PortfolioParameterSerializer
    queryset = PortfolioParameter.objects.all()

    def get_permissions(self):
        return OwnerCUD_AuthR(self, super())

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.all()


class PortfolioLogEntryViewSet(viewsets.ModelViewSet):

    serializer_class = PortfolioLogEntrySerializer
    queryset = PortfolioLogEntry.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.all()


class PortfolioAssetView(viewsets.ModelViewSet):

    permission_classes = [IsOwner]

    serializer_class = PortfolioAssetSerializer
    queryset = PortfolioAsset.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.all()


class PortfolioPositionView(viewsets.ModelViewSet):

    permission_classes = [IsOwner]

    serializer_class = PortfolioPositionSerializer
    queryset = PortfolioPosition.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        asset = instance.asset
        self.perform_destroy(instance)

        if not self.queryset.filter(asset=asset):
            asset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
