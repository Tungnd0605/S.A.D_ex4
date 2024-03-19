from django.urls import path, include
from . import views
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'managerapi', ManagerViewSet)

urlpatterns=[
    path('', include(router.urls)),
    path('manager/<int:id>', views.manager_detail, name='manager_detail')
]