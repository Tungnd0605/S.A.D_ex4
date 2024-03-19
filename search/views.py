from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse
from book.models import Book
from mobile.models import Mobile
from clothes.models import Clothes

# Create your views here.
def search(request, keyword):
    books = Book.objects.filter(title__icontains=keyword).values()
    mobiles = Mobile.objects.filter(title__icontains=keyword).values()
    clothes = Clothes.objects.filter(title__icontains=keyword).values()
    template = loader.get_template('search_result.html')
    context = {
        'books': books,
        'mobiles': mobiles,
        'clothes': clothes,
    }
    return HttpResponse(template.render(context, request))


