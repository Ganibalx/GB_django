from django.urls import path
from .views import OrderList


urlpatterns = [
    path('client/<int:pk>/', OrderList.as_view(), name='orderlist'),
]
