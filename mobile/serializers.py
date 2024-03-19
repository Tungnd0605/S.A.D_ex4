from rest_framework import serializers
from .models import Mobile

class MobileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mobile
        fields = ('title', 'brand', 'price', 'stock', 'sold', 'cover')