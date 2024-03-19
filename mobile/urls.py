from django.urls import path, include
from . import views
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'mobileapi', MobileViewSet)

urlpatterns=[
    path('', include(router.urls)),
    path('mobile/<int:id>', views.mobile_detail, name='mobile_detail')
]