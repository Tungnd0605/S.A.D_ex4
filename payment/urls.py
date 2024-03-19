from django.urls import path
from .views import payment_details, thank_you

app_name = 'payment'


urlpatterns=[
    path('payment/<int:order_id>/', payment_details, name='payment_details'),
    path('thank-you/', thank_you, name='thank_you'),
]

