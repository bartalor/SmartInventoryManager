from django.urls import path
from django.contrib import admin
from .views import CustomerView, TransactionView, ProductView, OrderView, home
from .views.home import home

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),  # Home page route
    path("products/", ProductView.as_view(), name='products'),
    path('customers/', CustomerView.as_view(), name='customers'),
    path('transactions/', TransactionView.as_view(), name='transactions'),
    path('orders/', OrderView.as_view(), name='orders'),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
]