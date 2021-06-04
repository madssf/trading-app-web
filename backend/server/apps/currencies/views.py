from apps.users.permissions import AdminCUD_AuthR
from .models import Currency, MCAPTotal, Tag, TagGroup, CurrencyTag
from .serializers import CurrencySerializer, MCAPTotalSerializer, TagSerializer, TagGroupSerializer, CurrencyTagSerializer
from rest_framework import viewsets


class CurrencyViewSet(viewsets.ModelViewSet):

    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()

    def get_permissions(self):
        return AdminCUD_AuthR(self, super())

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

    def get_queryset(self):
        return self.queryset.all()


class TagGroupViewSet(viewsets.ModelViewSet):

    serializer_class = TagGroupSerializer
    queryset = TagGroup.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return self.queryset.all()


class TagViewSet(viewsets.ModelViewSet):

    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return self.queryset.all()


class CurrencyTagViewSet(viewsets.ModelViewSet):

    serializer_class = CurrencyTagSerializer
    queryset = CurrencyTag.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return self.queryset.all()


class MCAPTotalViewSet(viewsets.ModelViewSet):

    serializer_class = MCAPTotalSerializer
    queryset = MCAPTotal.objects.all()

    def get_permissions(self):
        return AdminCUD_AuthR(self, super())

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

    def get_queryset(self):
        return self.queryset.all()
