from django.shortcuts import render
from rest_framework import generics
from . import serializers, models

# Create your views here.
class KittyList(generics.ListAPIView): 
    serializer_class = serializers.KittySerializer
    queryset = models.Kitty.objects.all()