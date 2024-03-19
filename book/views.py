from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from django.http import HttpResponse
from django.template import loader


# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def book_detail(request, id):
    book = Book.objects.get(id=id)
    template = loader.get_template('detail.html')
    context = {
        'book': book
    }
    return HttpResponse(template.render(context, request))
