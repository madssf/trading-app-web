from rest_framework import viewsets
from .models import Exchange
from .serializers import ExchangeSerializer
from apps.users.permissions import AdminCUD_AnyR


class ExchangeViewSet(viewsets.ModelViewSet):

    serializer_class = ExchangeSerializer
    queryset = Exchange.objects.all()

    def get_permissions(self):
        return AdminCUD_AnyR(self, super())

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

    def get_queryset(self):
        return self.queryset.all()
