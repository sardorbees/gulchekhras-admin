from django.db import models

class Video(models.Model):
    video = models.FileField(upload_to='videos/', verbose_name="Видео")

    def __str__(self):
        return f"Видео {self.id}"


    verbose_name = "Видео вашы работы"
    verbose_name_plural = "Видео вашы работы"