from django.db import models


class Product(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=255
    )
    description = models.TextField(
        'Описание'
    )
    link = models.URLField(
        'Ссылка',
        max_length=1024
        )
    price = models.CharField(
        'Цена',
        max_length=50
    )
    original_price = models.CharField(
        'Цена до скидки',
        max_length=50
    )
    image = models.URLField(
        'Изображение товара',
        max_length=1024
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class ParserConfiguration(models.Model):
    products_count = models.PositiveIntegerField(
        'Количество продуктов для парсинга',
        default=10,
    )
    pub_date = models.DateTimeField(
        'Дата парсинга',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Конфигурация парсера'
        verbose_name_plural = 'Конфигурации парсера'

    def __str__(self):
        return (f'Конфигурация парсинга (количество продуктов: '
                f'{self.products_count})')
