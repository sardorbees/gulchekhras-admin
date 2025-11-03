from django.db import models

class Application(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Полное имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    question = models.TextField(verbose_name="Вопрос")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    def __str__(self):
        return f"{self.full_name} — {self.phone}"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
