from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import RegisterSerializer, UserProfileSerializer
from .models import Address
from .serializers import AddressSerializer

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class UserProfileView(RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)  # частичное обновление
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response({"detail": "Вы вышли"}, status=status.HTTP_200_OK)

class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Добро пожаловать, {request.user.first_name}!"})

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, serializers

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        old_password = serializer.validated_data["old_password"]
        new_password = serializer.validated_data["new_password"]

        if not user.check_password(old_password):
            return Response({"error": "Неверный текущий пароль"}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()

        return Response({"detail": "Пароль успешно изменён ✅"})

from .utils import send_sms_eskiz


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()

            # Отправка SMS
            if hasattr(user, 'phone_number'):
                message = "Ваш пароль был успешно изменён."
                send_sms_to_user(user.phone_number, message)

            return Response({"message": "Пароль успешно изменён"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


import requests

def send_sms_to_user(phone, message):
    try:
        token_response = requests.post('https://notify.eskiz.uz/api/auth/login', data={
            'email': 'ваш_email',
            'password': 'ваш_пароль',
        })
        token = token_response.json()['data']['token']

        requests.post('https://notify.eskiz.uz/api/message/sms/send', data={
            'mobile_phone': phone,
            'message': message,
            'from': '4546',  # или ваше значение
            'callback_url': 'http://yourdomain.uz/callback/',
        }, headers={'Authorization': f'Bearer {token}'})
    except Exception as e:
        print('Ошибка при отправке SMS:', e)

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Address
from .serializers import AddressSerializer

class AddressListCreateView(ListCreateAPIView):
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Возвращаем только адреса текущего пользователя
        return Address.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # При создании автоматически привязываем адрес к текущему пользователю
        serializer.save(user=self.request.user)

class AddressDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'address_id'

    def get_queryset(self):
        # Доступ только к своим адресам
        return Address.objects.filter(user=self.request.user)