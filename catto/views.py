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


        if 'name' in query.keys() and 'tags' and 'type' in query.keys():
            return models.Kitty.objects.filter(Q(name=query['name'])&Q(tags__icontains=query['tags'])&Q(img__endswith=query['type'])).order_by('?')

        if 'name' in query.keys():
            if 'tags' in query.keys():
                return models.Kitty.objects.filter(Q(name=query['name'])&Q(tags__icontains=query['tags'])).order_by('?')
            
            if 'type' in query.keys():
                return models.Kitty.objects.filter(Q(name=query['name'])&Q(img__endswith=query['type'])).order_by('?')

            return models.Kitty.objects.filter(Q(name=query['name'])).order_by('?')

        if 'tags' in query.keys():
            if 'type' in query.keys():
                return models.Kitty.objects.filter(Q(tags__icontains=query['tags'])&Q(img__endswith=query['type'])).order_by('?')

            return models.Kitty.objects.filter(Q(tags__icontains=query['tags'])).order_by('?')

        if 'type' in query.keys():
            return models.Kitty.objects.filter(Q(img__endswith=query['type'])).order_by('?')


        


def PickCatto(request):
    pks =  models.Kitty.objects.values_list('pk', flat=True)
    pk = random.choice(pks)
    return redirect(reverse('kitties')+r'catto/{}/'.format(str(pk)))