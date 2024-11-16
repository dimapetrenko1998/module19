from django.urls import path
from .views import home, products, cart, register, login_view

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('cart/', cart, name='cart'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
]

