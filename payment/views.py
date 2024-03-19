from django.shortcuts import render, redirect
from .models import Payment
from checkout.models import Checkout

def payment_details(request, order_id):
    if request.method == 'POST':
        order = Checkout.objects.get(id=order_id)
        payment_method = request.POST.get('payment_method')
        payment_details = request.POST.get('payment_details')
        Payment.objects.create(order=order, payment_method=payment_method, payment_details=payment_details)
        return render(request, 'thank_you.html')
    else:
        order = Checkout.objects.get(id=order_id)
        return render(request, 'payment_details.html', {'order': order})

def thank_you(request):
    return render(request, 'thank_you.html')
