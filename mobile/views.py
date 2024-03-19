from django.shortcuts import render
from .models import Mobile
from .serializers import MobileSerializer
from rest_framework import viewsets
from django.http import HttpResponse
from django.template import loader
# Create your views here.

class MobileViewSet(viewsets.ModelViewSet):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer

def mobile_detail(request, id):
    mobile = Mobile.objects.get(id=id)
    template = loader.get_template('mobile-detail.html')
    context = {
        'mobile': mobile
    }
    return HttpResponse(template.render(context, request))