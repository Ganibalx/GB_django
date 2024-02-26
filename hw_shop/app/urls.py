from django.urls import path
from .views import OrderList, ProductBase, CreateProduct, UpdateProduct


urlpatterns = [
    path('client/<int:pk>/', OrderList.as_view(), name='orderlist'),
    path('product/', ProductBase.as_view(), name='products'),
    path('product/add/', CreateProduct.as_view(), name='addproduct'),
    path('product/update/<int:pk>', UpdateProduct.as_view(), name='updateproduct')
]
