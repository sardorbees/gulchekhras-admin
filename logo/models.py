# models.py
from django.db import models
import os

def category_image_path(instance, filename):
    return os.path.join('assets', 'img', filename)

class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=category_image_path, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Лого'
        verbose_name_plural = 'Лого'
