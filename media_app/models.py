from django.db import models

def image_upload_to(instance, filename):
    return f'images/{filename}'

def video_upload_to(instance, filename):
    return f'videos/{filename}'

class MediaItem(models.Model):
    title = models.CharField(max_length=255, verbose_name=("заголовок"))
    desc = models.TextField(blank=True, verbose_name=("описание"))
    image = models.ImageField(upload_to=image_upload_to, blank=True, null=True, verbose_name=("изображение"))
    video = models.FileField(upload_to=video_upload_to, blank=True, null=True, verbose_name=("видео"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=("создано_at"))

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
