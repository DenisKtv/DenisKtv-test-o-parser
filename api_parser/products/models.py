from django.db import models


class Product(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=255
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    link = models.URLField(
        verbose_name='Ссылка',
        max_length=1024
        )
    price = models.CharField(
        verbose_name='Цена',
        max_length=50
    )
    original_price = models.CharField(
        verbose_name='Цена до скидки',
        max_length=50
    )
    image = models.URLField(
        verbose_name='Изображение товара',
        max_length=1024
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title
