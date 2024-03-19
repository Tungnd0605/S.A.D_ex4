from django.shortcuts import render
from .models import Clothes
from .serializers import ClothesSerializer
from rest_framework import viewsets
from django.http import HttpResponse
from django.template import loader
# Create your views here.

class ClothesViewSet(viewsets.ModelViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer

def clothes_detail(request, id):
    clothes = Clothes.objects.get(id=id)
    template = loader.get_template('clothes-detail.html')
    context = {
        'clothes': clothes
    }
    return HttpResponse(template.render(context, request))