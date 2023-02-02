from django.shortcuts import render
from django.http import Http404

from .serializers import ImageSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Image, Category
from .serializers import ImageSerializer, UploadSerializer



class LatestImageList(APIView):
    def get(self, request, format=None):
        images = Image.objects.all()[0:4]
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)


class ImageDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Image.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Image.DoesNotExist:
            return Http404

    def get(self, request, category_slug, image_slug, format=None):
        image = self.get_object(category_slug, image_slug)
        serializer = ImageSerializer(image)
        return Response(serializer.data)


@api_view(['POST'])
def upload_photo(request):
    print(request.data)
    # udało się tym przesłać zdjęcie
    category = Category.objects.first()
    img = Image(
        category=category,
        name='bob',
        slug='bob',
        description='my cat',
        image=request.data['image']
    )
    img.save()
    return Response('success')
