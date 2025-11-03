from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from .models import Product, Category, Color, Size, DressType
from .serializers import ProductSerializer, CategorySerializer, ColorSerializer, SizeSerializer, DressTypeSerializer

from django.db.models import Count
from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.annotate(product_count=Count('products'))
    serializer_class = CategorySerializer

class ColorListView(APIView):
    def get(self, request):
        colors = Color.objects.all()
        serializer = ColorSerializer(colors, many=True)
        return Response(serializer.data)

class SizeListView(APIView):
    def get(self, request):
        sizes = Size.objects.all()
        serializer = SizeSerializer(sizes, many=True)
        return Response(serializer.data)

class DressTypeListView(APIView):
    def get(self, request):
        dresses = DressType.objects.all()
        serializer = DressTypeSerializer(dresses, many=True)
        return Response(serializer.data)

# Список продуктов с фильтрацией
class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()

        category = request.GET.get('category')
        color = request.GET.get('color')
        size = request.GET.get('size')
        dress = request.GET.get('dress')
        rating = request.GET.get('rating')
        price_min = request.GET.get('price_min')
        price_max = request.GET.get('price_max')

        if category:
            ids = [int(x) for x in category.split(',')]
            products = products.filter(category_id__in=ids)
        if color:
            ids = [int(x) for x in color.split(',')]
            products = products.filter(color_id__in=ids)
        if size:
            ids = [int(x) for x in size.split(',')]
            products = products.filter(size_id__in=ids)
        if dress:
            ids = [int(x) for x in dress.split(',')]
            products = products.filter(dress_id__in=ids)
        if rating:
            products = products.filter(rating__gte=int(rating))
        if price_min:
            products = products.filter(price__gte=float(price_min))
        if price_max:
            products = products.filter(price__lte=float(price_max))

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductSearchView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '').strip()
        if query:
            # фильтр по первой букве (без учёта регистра)
            return Product.objects.filter(title__istartswith=query)
        return Product.objects.all()


from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer