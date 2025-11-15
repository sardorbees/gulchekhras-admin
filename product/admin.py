from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_new", "in_stock", "created_at")
    search_fields = ("name",)
    list_filter = ("is_new", "in_stock")
