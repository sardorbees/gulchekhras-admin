from django.db import models

# ======== Фильтры ========
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="URL slug")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Color(models.Model):
    name = models.CharField(max_length=50, verbose_name="Цвет одежды")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"


class Size(models.Model):
    name = models.CharField(max_length=10, verbose_name="Размер одежды")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"


class DressType(models.Model):
    name = models.CharField(max_length=50, verbose_name="Тип одежды (Мужской, Женский и т.д.)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип одежды"
        verbose_name_plural = "Типы одежды"


# ======== Продукт ========
class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Старая цена")
    img = models.ImageField(upload_to="product/", verbose_name="Фото товара")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name="products")
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="products")
    dress = models.ForeignKey(DressType, on_delete=models.CASCADE, related_name="products")
    rating = models.IntegerField(default=1)
    reviews = models.IntegerField(default=0)
    popularity = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
