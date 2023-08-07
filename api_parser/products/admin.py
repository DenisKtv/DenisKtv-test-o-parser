from django.contrib import admin
from .models import Product


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
    search_fields = ('title',)
    ordering = ('id',)

    def short_description(self, obj):
        return (obj.description[:200] + '...' if len(obj.description) > 200
                else obj.description)
    short_description.short_description = 'Описание'
