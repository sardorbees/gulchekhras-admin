# yourapp/views.py
import requests
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from .forms import TelegramMessageForm

def send_telegram_message(chat_id, message):
    bot_token = settings.TELEGRAM_BOT_TOKEN
    url = f"https://api.telegram.org/bot{7292828359:AAGZ5DjUUMQkqecQDziGBFGEmhuWL2NMOcs}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=payload)
    return response

def send_message_view(request):
    if request.method == 'POST':
        form = TelegramMessageForm(request.POST)
        if form.is_valid():
            chat_id = form.cleaned_data['chat_id']
            message = form.cleaned_data['message']
            response = send_telegram_message(chat_id, message)
            if response.status_code == 200:
                return HttpResponse("Message sent successfully!")
            else:
                return HttpResponse("Failed to send message.")
    else:
        form = TelegramMessageForm()
    return render(request, 'send_message.html', {'form': form})
