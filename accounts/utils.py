import requests

def send_sms_eskiz(phone_number, message):
    token = "ВАШ_EKIZ_TOKEN"
    url = "https://notify.eskiz.uz/api/message/sms/send"

    headers = {
        "Authorization": f"Bearer {token}",
    }

    data = {
        "mobile_phone": phone_number,
        "message": message,
        "from": "4546",  # это код отправителя (можно оставить как есть)
        "callback_url": ""
    }

    response = requests.post(url, headers=headers, data=data)
    return response.json()
