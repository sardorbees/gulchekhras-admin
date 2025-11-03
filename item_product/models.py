from django.db import models
from django.utils.text import slugify

class Item(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название категории")
    desc = models.TextField(verbose_name="описание")
    slug = models.SlugField(unique=True, blank=True, verbose_name="url shop-category")
    img = models.ImageField(upload_to='items/', verbose_name="Фото")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    verbose_name = "Купить по категории"
    verbose_name_plural = "Купить по категории"
