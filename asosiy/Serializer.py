from rest_framework import serializers
from .models import *

class MahsulotSer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'

class ClientSer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'