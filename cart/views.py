from django.shortcuts import render, redirect
from .models import CartItem
from book.models import Book
from clothes.models import Clothes
from mobile.models import Mobile
from django.contrib.auth.decorators import login_required


@login_required
def add_to_cart(request, product_type, product_id, quantity):
    if product_type == 'book':
        product = Book.objects.get(pk=product_id)
    elif product_type == 'clothes':
        product = Clothes.objects.get(pk=product_id)
    elif product_type == 'mobile':
        product = Mobile.objects.get(pk=product_id)
    if request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product_id = product_id,
                                                             product_name = product.title,
                                                             product_price = product.price)
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            cart_item.quantity = quantity
            cart_item.save()
        return redirect('cart:cart_view')
    else:
        return redirect("/")

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product_price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(pk=cart_item_id)
    cart_item.delete()
    return redirect('cart:cart_view')


# Create your views here.
