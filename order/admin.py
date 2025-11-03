from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'customer_phone', 'total_price', 'created_at')
    inlines = [OrderItemInline]
    search_fields = ('customer_name', 'customer_phone')
    list_filter = ('created_at',)
