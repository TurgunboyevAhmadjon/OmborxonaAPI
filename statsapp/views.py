from requests import Response
from .Serializer import *
from rest_framework import generics


class StatsListCreate(generics.ListCreateAPIView):
    queryset = Stats.objects.all()
    serializer_class = StatsSerializer

    def get(self, request):
        ombor = Ombor.objects.get(user=request.user)
        stats = Stats.objects.filter(ombor=ombor)
        ser = StatsSerializer(stats, many=True)
        return Response(ser.data)

    def post(self, request):
        ombor = Ombor.objects.get(user=request.user)
        malumot = request.data
        ser = StatsSerializer(data=malumot)
        if ser.is_valid():
            ser.save(profil=ombor)
        return Response(ser.data)

class StatsUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stats.objects.all()
    serializer_class = StatsSerializer