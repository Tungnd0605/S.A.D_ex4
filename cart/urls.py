from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart/', views.view_cart, name='cart_view'),
    path('add/<str:product_type>/<int:product_id>/<int:quantity>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
