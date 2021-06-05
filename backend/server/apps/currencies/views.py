from apps.users.permissions import AdminCUD_AuthR
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from .models import Currency, MCAPTotal, Tag, TagGroup, CurrencyTag
from .serializers import CurrencySerializer, MCAPTotalSerializer, TagSerializer, TagGroupSerializer, CurrencyTagSerializer


class CurrencyViewSet(viewsets.ModelViewSet):

    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()

    def get_permissions(self):
        return AdminCUD_AuthR(self, super())

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

    def get_queryset(self):
        return self.queryset.all()

    def perform_update(self, serializer):
        serializer.save()


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


class CurrencyBatchViewSet(viewsets.ViewSet):

    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

    @action(detail=True, methods=['post'])
    def batch_update(self, request, pk=None):

        recent_users = User.objects.all().order_by('-last_login')

        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)


class CurrencyBatchView(APIView):
    """
    A view that can accept POST requests with JSON content.
    """
    permission_classes = [IsAdminUser]
    parser_classes = [JSONParser]

    def post(self, request, format=None):
        return Response({'received data': request.data})
