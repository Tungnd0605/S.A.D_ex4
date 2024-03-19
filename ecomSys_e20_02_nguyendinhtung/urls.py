from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('book.urls')),
    path('', include('cart.urls')),
    path('', include('clothes.urls')),
    path('', include('manager.urls')),
    path('', include('mobile.urls')),
    path('', include('payment.urls')),
    path('', include('search.urls')),
    path('', include('user.urls')),
    path('', include('homepage.urls')),
    path('', include('checkout.urls')),
    path('', include('delivery.urls')),
    path('admin/', admin.site.urls),
]
