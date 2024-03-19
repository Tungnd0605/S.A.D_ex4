from rest_framework import serializers
from .models import Clothes

class ClothesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clothes
        fields = ('title', 'brand', 'price', 'stock', 'sold', 'cover')