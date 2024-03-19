from django.shortcuts import render
from .models import Manager
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .serializers import ManagerSerializer
from django.template import loader
from django.http import HttpResponse

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

def manager_detail(request, id):
    manager = Manager.objects.get(id=id)
    template = loader.get_template('manager-detail.html')
    context = {
        'manager': manager
    }
    return HttpResponse(template.render(context, request))