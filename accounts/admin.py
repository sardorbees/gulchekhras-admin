from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Address

class AddressInline(admin.TabularInline):
    model = Address
    extra = 1  # сколько пустых форм для добавления показывать
    fields = ('street', 'city', 'country')
    # Можно запретить удалять или редактировать, если нужно

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Дополнительно", {"fields": ("phone_number", "image")}),
    )
    list_display = ("username", "password", "phone_number")
    inlines = [AddressInline]  # Добавляем inline с адресами
