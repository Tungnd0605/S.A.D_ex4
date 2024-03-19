from rest_framework import serializers
from .models import Manager


class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields = ('name', 'email', 'phone', 'password', 'address')
