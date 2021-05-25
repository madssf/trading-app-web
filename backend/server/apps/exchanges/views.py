from rest_framework import viewsets
from .models import Exchange, Credentials
from .serializers import ExchangeSerializer, CredentialsSerializer


class ExchangeViewSet(viewsets.ModelViewSet):

    serializer_class = ExchangeSerializer
    queryset = Exchange.objects.all()

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

    def get_queryset(self):
        return self.queryset.all()


class CredentialsViewSet(viewsets.ModelViewSet):

    serializer_class = CredentialsSerializer
    queryset = Credentials.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
