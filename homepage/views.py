from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from book.models import Book
from clothes.models import Clothes
from mobile.models import Mobile

def index(request):
    books = Book.objects.all().values()
    clothes = Clothes.objects.all().values()
    mobiles = Mobile.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'books': books,
        'mobiles': mobiles,
        'clothes': clothes,

    }
    return HttpResponse(template.render(context, request))

