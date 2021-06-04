from rest_framework import serializers
from .models import Currency, CurrencyTag, Price, Tag, TagGroup, MCAPTotal


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = '__all__'


class TagGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = TagGroup
        fields = ["created_at", "created_by", "name", "description"]


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ["created_at", "created_by",
                  "tag_group", "name", "description"]


class CurrencyTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = CurrencyTag
        fields = ['tag', 'currency']


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['timestamp', 'currency', 'open',
                  'high', 'low', 'close', 'volume']


class MCAPTotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCAPTotal
        fields = '__all__'
