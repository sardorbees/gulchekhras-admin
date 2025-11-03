from django import forms

class TelegramMessageForm(forms.Form):
    chat_id = forms.CharField(label='Chat ID', max_length=255)
    message = forms.CharField(label='Message', widget=forms.Textarea)