from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Checkout
from cart.models import CartItem

@login_required
def checkout(request):
    if request.method == 'POST':
        # Process order creation and save to database
        cart_items = CartItem.objects.filter(user=request.user)
        total_amount = sum(item.product_price * item.quantity for item in cart_items)
        order = Checkout.objects.create(user=request.user, total_amount=total_amount)
        # Clear the cart after placing the order
        cart_items.delete()
        return redirect('order:order_confirmation', order_id=order.id)
    else:
        cart_items = CartItem.objects.filter(user=request.user)
        total_amount = sum(item.product_price * item.quantity for item in cart_items)
        return render(request, 'checkout.html', {'cart_items': cart_items, 'total_amount': total_amount})

@login_required
def order_confirmation(request, order_id):
    order = Checkout.objects.get(id=order_id)
    return render(request, 'order_confirmation.html', {'order': order})
