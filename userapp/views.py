from django.shortcuts import render
from rest_framework.response import Response

from .serializer import OmborSerializer
from .models import Ombor
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.views import APIView

class OmborAPIView(APIView):
    def get(self, request):
        ombor = Ombor.objects.all()
        serializer =OmborSerializer(ombor, many=True)
        return Response(serializer.data)

