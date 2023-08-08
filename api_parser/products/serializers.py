from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.URLField(source='image')
    discount = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'title', 'price', 'discount', 'image_url', 'description'
        )

    def get_discount(self, obj):
        original_price = float(
            obj.original_price.replace(',', '.').replace(' BYN', '')
        )
        price = float(obj.price.replace(',', '.').replace(' BYN', ''))
        disc = (original_price - price) / original_price * 100
        return f'{round(disc, 1)}%'
