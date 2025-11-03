from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='gallery/', verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    def __str__(self):
        return f"Фото #{self.id}"

    class Meta:
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификат"
