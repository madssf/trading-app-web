from rest_framework import serializers
from .models import TagGroup, Tag


class TagGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = TagGroup
        read_only_fields = (
            "id",
            "created_at",
            "created_by",
        )
        fields = (
            "id",
            "created_at",
            "created_by",
            "name",
            "description"
        )


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        read_only_fields = (
            "id",
            "created_at",
            "created_by",
        )
        fields = (
            "id",
            "created_at",
            "created_by",
            "tag_group",
            "name",
            "description"
        )
