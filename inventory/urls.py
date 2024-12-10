from django.urls import path
from inventory.views import CustomerView, TransactionView

urlpatterns = [
    path('customers/', CustomerView.as_view(), name='customers'),
    path('transactions/', TransactionView.as_view(), name='transactions'),
]