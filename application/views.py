from rest_framework import generics, status
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta, datetime
from django.core.cache import cache
from pytz import timezone as django_timezone
import requests

from .models import Application
from .serializers import ApplicationSerializer

# 🔹 Токен и чат ID Telegram
TELEGRAM_TOKEN = '8013655006:AAGBb-a4EIlgLo9qA4NObowsesvOZ_hQkQI'
TELEGRAM_CHAT_ID = '1756108441'


class ApplicationCreateView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def create(self, request, *args, **kwargs):
        phone = request.data.get('phone')

        # Ограничение по номеру: 1 заявка в 2 минуты
        redis_key = f'form_block_phone_{phone}'
        if cache.get(redis_key):
            return Response(
                {"detail": "Вы уже отправляли заявку. Повторите через 2 минуты."},
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )

        # Проверяем, была ли заявка с этим номером за последние 2 минуты
        if Application.objects.filter(
            phone=phone,
            created_at__gte=timezone.now() - timedelta(minutes=2)
        ).exists():
            return Response(
                {"detail": "С этого номера уже отправляли заявку. Повторите через 2 минуты."},
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )

        # Сохраняем заявку
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        application = serializer.save()

        # Устанавливаем блокировку по номеру на 2 минуты
        cache.set(redis_key, '1', timeout=60 * 2)

        # Отправляем уведомление в Telegram
        self.send_telegram_notification(application)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def send_telegram_notification(self, application):
        # Часовой пояс Узбекистана
        uz_time = datetime.now(django_timezone('Asia/Tashkent'))
        if 9 <= uz_time.hour <= 20:  # Только с 9:00 до 20:00
            message = (
                f"📥 Новая заявка на solar-energy\n"
                f"👤 Имя: {application.full_name}\n"
                f"📞 Телефон: {application.phone}\n"
                f"💬 Вопрос: {application.question}\n"
            )
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
            requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": message})
