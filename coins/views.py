from django.shortcuts import render
from .models import Coins
from rest_framework import generics
from .serializers import CoinsSerializer

# Create your views here.


class CoinsAPIView(generics.ListAPIView):
    queryset = Coins.objects.all()
    serializer_class = CoinsSerializer
