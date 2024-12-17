from django.urls import path
from .views.home import home
from .views.logout_view import logout_view
from .views.store import store, purchase_product
from .views.register_view import register
from django.contrib.auth.views import LoginView
from django.contrib import admin

urlpatterns = [
    path("", home, name="home"),
    path('admin/', admin.site.urls),
    path("store/", store, name="store"),
    path("purchase/<int:product_id>/", purchase_product, name="purchase_product"),
    path("login/", LoginView.as_view(template_name="login.html", next_page="home"), name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register, name="register"),
]
