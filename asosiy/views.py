from rest_framework.views import APIView

from .Serializer import *
from .models import *
from userapp.serializer import *
from rest_framework import generics

class OmborAPIView(APIView):
    queryset = Ombor.objects.all()
    serializer_class = OmborSerializer

class ClientListCreate(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSer

class ClientUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSer

class MahsulotListCreate(generics.ListCreateAPIView):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSer

class MahsulotUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSer