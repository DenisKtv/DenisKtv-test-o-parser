from django.contrib import admin
from django.urls import path
from products.views import ProductListView, ProductDetailView, StartParsingView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'v1/products/',
        StartParsingView.as_view(),
        name='start-parsing'
    ),
    path('v1/products/', ProductListView.as_view(), name='product-list'),
    path(
        'v1/products/<int:pk>/',
        ProductDetailView.as_view(),
        name='product-detail'
    ),
]
