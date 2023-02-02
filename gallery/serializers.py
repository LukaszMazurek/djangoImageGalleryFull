from rest_framework import serializers

from .models import Category, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            "id",
            "name",
            "description",
            "slug",
            "get_image",
            "get_thumbnail",
            "get_absolute_url"
        )


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        mode = Image
        fields = (
            "image",
        )