from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# 🔐 Пользователь
class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone']

    def __str__(self):
        return self.username

# 🏠 Адрес пользователя
class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='addresses')
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100, default="Uzbekistan")

    def __str__(self):
        return f"{self.street}, {self.city}"

# 📦 Заказ пользователя
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"
