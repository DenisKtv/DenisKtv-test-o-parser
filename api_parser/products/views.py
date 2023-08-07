from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .tasks import parse_products
from .serializers import ProductSerializer
from .models import Product
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class StartParsingView(APIView):
    def post(self, request):
        products_count = request.data.get('products_count', 10)
        products_count = min(int(products_count), 50)

        parse_products.delay(products_count)

        return Response(
            {'status': 'parsing started'},
            status=status.HTTP_202_ACCEPTED
        )


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
