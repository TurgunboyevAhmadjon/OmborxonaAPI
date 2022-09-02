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




class KursAPIView(APIView):
    def get(self, request):
        pr = Profil.objects.get(user=request.user)
        xaridlar = pr.profil_xaridlari.all()
        kurslar = Kurs.objects.filter(id__in=[xarid.kurs.id for xarid in xaridlar])
        kurslar = kurslar | Kurs.objects.filter(bepul=True)
        ser = KursSer(kurslar, many=True)
        return Response(ser.data)

class TanlanganAPIView(APIView):
    def get(self, request):
        pr = Profil.objects.get(user=request.user)
        tanlanganlar = Tanlangan.objects.filter(profil=pr)
        ser = TanlanganSer(tanlanganlar, many=True)
        return Response(ser.data)
    def post(self, request):
        pr = Profil.objects.get(user=request.user)
        malumot = request.data
        ser = TanlanganSer(data=malumot)
        if ser.is_valid():
            ser.save(profil=pr)
        return Response(ser.data)