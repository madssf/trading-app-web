from rest_framework import viewsets, mixins, generics
from .models import Strategy, ParameterType, Parameter, StrategyParameter
from .serializers import StrategySerializer, ParameterTypeSerializer, ParameterSerializer, StrategyParameterSerializer
from apps.users.permissions import AdminCUD_AuthR


class StrategyViewSet(viewsets.ModelViewSet):

    serializer_class = StrategySerializer
    queryset = Strategy.objects.all()

    def get_permissions(self):
        return AdminCUD_AuthR(self, super())

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return self.queryset.all()


class ParameterTypeViewSet(viewsets.ModelViewSet):

    serializer_class = ParameterTypeSerializer
    queryset = ParameterType.objects.all()

    def get_permissions(self):
        return AdminCUD_AuthR(self, super())

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return self.queryset.all()


class ParameterViewSet(viewsets.ModelViewSet):

    serializer_class = ParameterSerializer
    queryset = Parameter.objects.all()

    def get_permissions(self):
        return AdminCUD_AuthR(self, super())

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return self.queryset.all()


class StrategyParameterViewSet(viewsets.ModelViewSet):

    serializer_class = StrategyParameterSerializer
    queryset = StrategyParameter.objects.all()

    def get_permissions(self):
        return AdminCUD_AuthR(self, super())

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return self.queryset.all()
