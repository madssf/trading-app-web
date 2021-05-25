from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import TagGroup, Tag
from .serializers import TagGroupSerializer, TagSerializer


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
