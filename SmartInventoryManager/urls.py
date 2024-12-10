from django.urls import path
from .views import CustomerView, TransactionView, ProductView, OrderView

urlpatterns = [
    path("products/", ProductView.as_view(), name='products'),
    path('customers/', CustomerView.as_view(), name='customers'),
    path('transactions/', TransactionView.as_view(), name='transactions'),
    path('orders/', OrderView.as_view(), name='orders'),
]