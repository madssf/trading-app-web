from django.http.response import JsonResponse
from apps.users.permissions import AdminCUD_AuthR
from .models import Currency, MCAPTotal, Tag, TagGroup, CurrencyTag
from .serializers import CurrencySerializer, MCAPTotalSerializer, TagSerializer, TagGroupSerializer, CurrencyTagSerializer
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from django.views.generic import CreateView, DetailView, UpdateView
from rest_framework.permissions import IsAdminUser

from .forms import CurrencyForm
from .models import Currency

'''
class CurrencyViewSet(viewsets.ModelViewSet):

    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()

    def get_permissions(self):
        return AdminCUD_AuthR(self, super())

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

    def get_queryset(self):
        return self.queryset.all()
'''


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


class CurrencyCreateView(LoginRequiredMixin, CreateView):

    model = Currency
    form_class = CurrencyForm

    def form_valid(self, form):
        currency = form.save(commit=False)

        try:
            Currency.objects.get(symbol=currency.symbol)
            return JsonResponse({'msg': 'already exists'}, safe=False)
        except Currency.DoesNotExist:
            currency.slug = slugify(currency.symbol)

            # Save again - this time to the database
            currency.save()
            return super().form_valid(form)


class CurrencyUpdateView(LoginRequiredMixin, UpdateView):
    model = Currency
    form_class = CurrencyForm
    permission_classes = [IsAdminUser]

    def get_object(self):
        return get_object_or_404(Currency,
                                 slug=self.kwargs['slug'],
                                 )

    def form_valid(self, form):
        # Update the slug if the symbol has changed.
        currency = form.save(commit=False)
        currency.slug = slugify(currency.symbol)
        currency.save()
        return super().form_valid(form)


class CurrencyDetailView(DetailView):
    model = Currency

    def get_object(self):
        return get_object_or_404(Currency,
                                 slug=self.kwargs['slug'],)
