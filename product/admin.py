from django.contrib import admin
from .models import Category, Color, Size, DressType, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product_count')

    def product_count(self, obj):
        return obj.products.count()
    product_count.short_description = "Количество товаров"


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product_count')

    def product_count(self, obj):
        return obj.products.count()
    product_count.short_description = "Количество товаров"


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product_count')

    def product_count(self, obj):
        return obj.products.count()
    product_count.short_description = "Количество товаров"


@admin.register(DressType)
class DressTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product_count')

    def product_count(self, obj):
        return obj.products.count()
    product_count.short_description = "Количество товаров"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'price', 'rating')
    list_filter = ('category', 'color', 'size', 'dress')
    search_fields = ('title',)
