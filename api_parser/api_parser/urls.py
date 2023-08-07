from django.contrib import admin
from django.urls import path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from products.views import ProductListView, ProductDetailView, StartParsingView


schema_view = get_schema_view(
   openapi.Info(
      title="My API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.myapp.com/terms/",
      contact=openapi.Contact(email="contact@myapp.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

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
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
]
