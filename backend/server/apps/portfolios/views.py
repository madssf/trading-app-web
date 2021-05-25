from rest_framework import viewsets
from .models import Portfolio, PortfolioParameter
from .serializers import PortfolioSerializer, PortfolioParameterSerializer


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
