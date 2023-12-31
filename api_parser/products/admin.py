from django.contrib import admin

from .models import ParserConfiguration, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'link',
        'price',
        'original_price',
        'image',
        'short_description',
    )
    ordering = ('id',)

    def short_description(self, obj):
        return (obj.description[:200] + '...' if len(obj.description) > 200
                else obj.description)
    short_description.short_description = 'Описание'


@admin.register(ParserConfiguration)
class ParserAdmin(admin.ModelAdmin):
    list_display = ('products_count', 'pub_date')
