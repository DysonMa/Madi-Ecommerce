"""Ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myshop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),  # TODO -> find ans
    path('<int:cat_id>/', views.index),
    path('login/', views.login),
    path('logout/', views.logout),
    path('userinfo/', views.userinfo),
    # path('register/', include('registration.backends.default.urls')),
    path('register/', views.sign_up, name='Register'),
    path('accounts/', include('allauth.urls')), # django-allauth網址
    path('filer/', include('filer.urls')),
    path('product/<int:product_id>/', views.product, name='product-url'),
    path('cart/', views.cart), # 購物車
    path('additem/<int:product_id>/<int:quantity>/', views.add_to_cart, name='additem-url'), # 購物車
    path('removeitem/<int:product_id>/', views.remove_from_cart, name='removeitem-url'), # 購物車
    path('order/', views.order),
    path('myorders/', views.my_orders),
]

# django-filer
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)