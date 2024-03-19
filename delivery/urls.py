from django.urls import path
from .views import shipment_details

app_name = 'delivery'

urlpatterns = [
    path('shipment/<int:order_id>/', shipment_details, name='shipment_details'),
]
