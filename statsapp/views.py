from requests import Response
from .Serializer import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class StatsListCreate(generics.ListCreateAPIView):
    queryset = Stats.objects.all()
    serializer_class = StatsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

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
    permission_classes = [IsAuthenticatedOrReadOnly]