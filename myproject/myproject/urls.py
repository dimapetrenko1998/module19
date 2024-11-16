"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views. Home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from task1.views import products, cart, register, home, login_view

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('cart/', cart, name='cart'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('blog/', include('blog.urls'))
]

