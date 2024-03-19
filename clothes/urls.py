from django.urls import path, include
from . import views
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'clothesapi', ClothesViewSet)

urlpatterns=[
    path('', include(router.urls)),
    path('clothes/<int:id>', views.clothes_detail, name='clothes_detail')
]