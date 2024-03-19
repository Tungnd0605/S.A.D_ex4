from django.urls import path, include
from . import views
from rest_framework import routers
from .views import *
router = routers.SimpleRouter()
router.register(r'bookapi', BookViewSet)

urlpatterns=[
    path('', include(router.urls)),
    path('book/<int:id>', views.book_detail, name='book_detail')
]