from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer
from .tasks import parse_products


class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        products_count = request.data.get('products_count', 10)
        products_count = min(int(products_count), 50)
        print(products_count)
        parse_products.delay(products_count)

        return Response(
            {'status': 'parsing started'},
            status=status.HTTP_202_ACCEPTED
        )


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
