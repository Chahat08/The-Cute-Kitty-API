from django.urls import reverse
from rest_framework import generics
from . import serializers, models
from django.shortcuts import redirect
import random

# Create your views here.
class KittyList(generics.ListAPIView): 
    serializer_class = serializers.KittySerializer
    queryset = models.Kitty.objects.all()


class KittyCat(generics.RetrieveAPIView):
    serializer_class = serializers.KittySerializer
    queryset = models.Kitty.objects.all()


def PickCatto(request):
    pks =  models.Kitty.objects.values_list('pk', flat=True)
    pk = random.choice(pks)
    return redirect(reverse('kitties')+r'catto/{}/'.format(str(pk)))