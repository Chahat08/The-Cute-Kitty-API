from django.urls import reverse
from rest_framework import generics
from . import serializers, models
from django.shortcuts import redirect
import random
from django.db.models import Q
from itertools import chain

# Create your views here.
class KittyList(generics.ListAPIView): 
    serializer_class = serializers.KittySerializer
    queryset = models.Kitty.objects.all()


class KittyCat(generics.RetrieveAPIView):
    serializer_class = serializers.KittySerializer
    queryset = models.Kitty.objects.all()


class SearchKittyCat(generics.ListAPIView):
    serializer_class = serializers.KittySerializer
    
    def get_queryset(self):
        query = self.request.GET

        name_list = list()
        breed_list = list()

        if 'name' in query.keys() and'breed' in query.keys():
            return models.Kitty.objects.filter(Q(name__icontains=query['name'])&Q(breed__icontains=query['breed']))

        if 'name' in query.keys():
            return models.Kitty.objects.filter(Q(name__icontains=query['name']))

        if 'breed' in query.keys():
            return models.Kitty.objects.filter(Q(breed__icontains=query['breed']))



        return set(chain(name_list, breed_list))
        


def PickCatto(request):
    pks =  models.Kitty.objects.values_list('pk', flat=True)
    pk = random.choice(pks)
    return redirect(reverse('kitties')+r'catto/{}/'.format(str(pk)))