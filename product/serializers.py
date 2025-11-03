from rest_framework import serializers
from .models import (
    Product, Category, Color, Size, DressType,
)


# ===============================
# FILTER SERIALIZERS (с подсчётом товаров)
# ===============================
class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'product_count']

    def get_product_count(self, obj):
        return obj.products.count()


class ColorSerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Color
        fields = ['id', 'name', 'product_count']

    def get_product_count(self, obj):
        return obj.products.count()


class SizeSerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Size
        fields = ['id', 'name', 'product_count']

    def get_product_count(self, obj):
        return obj.products.count()


class DressTypeSerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = DressType
        fields = ['id', 'name', 'product_count']

    def get_product_count(self, obj):
        return obj.products.count()


# ===============================
# PRODUCT SERIALIZER
# ===============================
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    color = ColorSerializer(read_only=True)
    size = SizeSerializer(read_only=True)
    dress = DressTypeSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
