import requests
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem
from .serializers import OrderSerializer

# 🔑 данные твоего Telegram-бота
BOT_TOKEN = "8013655006:AAGBb-a4EIlgLo9qA4NObowsesvOZ_hQkQI"
CHAT_ID = "@gulchekras"  # например: 123456789
# TELEGRAM_BOT_TOKEN = "8013655006:AAGBb-a4EIlgLo9qA4NObowsesvOZ_hQkQI"
# TELEGRAM_CHAT_ID = "1756108441"

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()

        # ✉️ Формируем текст для Telegram
        items_text = "\n".join(
            [f"📦 {item.product_name} — {item.quantity} x {item.price:,} UZS" for item in order.items.all()]
        )
        message = (
            f"🛒 <b>Новый заказ!</b>\n\n"
            f"👤 Имя: {order.customer_name}\n"
            f"📞 Телефон: {order.customer_phone}\n"
            f"📍 Адрес: {order.customer_address}\n\n"
            f"{items_text}\n\n"
            f"💰 <b>Общая сумма:</b> {order.total_price:,} UZS"
        )

        # 🚀 Отправляем в Telegram
        try:
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                data={"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"},
                timeout=5
            )
        except Exception as e:
            print("Ошибка при отправке в Telegram:", e)