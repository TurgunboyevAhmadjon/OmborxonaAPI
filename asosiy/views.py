from requests import Response
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

    def get(self, request):
        ombor = Ombor.objects.get(user=request.user)
        client = Client.objects.filter(ombor=ombor)
        ser = ClientSer(client, many=True)
        return Response(ser.data)

    def post(self, request):
        ombor = Ombor.objects.get(user=request.user)
        malumot = request.data
        ser = ClientSer(data=malumot)
        if ser.is_valid():
            ser.save(profil=ombor)
        return Response(ser.data)

class ClientUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSer

class MahsulotListCreate(generics.ListCreateAPIView):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSer

    def get(self, request):
        ombor = Ombor.objects.get(user=request.user)
        mahsulot = Mahsulot.objects.filter(ombor=ombor)
        ser = MahsulotSer(mahsulot, many=True)
        return Response(ser.data)

    def post(self, request):
        ombor = Ombor.objects.get(user=request.user)
        malumot = request.data
        ser = MahsulotSer(data=malumot)
        if ser.is_valid():
            ser.save(profil=ombor)
        return Response(ser.data)

class MahsulotUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSer




