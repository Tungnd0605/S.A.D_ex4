from django.shortcuts import render, redirect
from .models import Delivery
from checkout.models import Checkout
from django.urls import reverse


def shipment_details(request, order_id):
    if request.method == 'POST':
        # Process shipment details and save to database
        order = Checkout.objects.get(id=order_id)
        shipment_vendor = request.POST.get('shipment_vendor')
        address = request.POST.get('address')
        Delivery.objects.create(order=order, shipment_vendor=shipment_vendor, address=address)
        return redirect(reverse('payment:payment_details', args=[order_id]))
    else:
        order = Checkout.objects.get(id=order_id)
        return render(request, 'shipment_details.html', {'order': order})
