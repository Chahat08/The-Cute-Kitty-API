from django.urls import reverse
from rest_framework import generics
from . import serializers, models
from django.shortcuts import redirect
import random
from django.db.models import Q

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

        evalstr = ''

        if 'tags' in query:
            tagslist = query.getlist('tags')
            evalstr += 'Q(tags__icontains=tagslist[0])'
            for i in range(1, len(tagslist)):
                evalstr += ' & Q(tags__icontains=tagslist[{}])'.format(str(i))


        if 'type' in query:
            typelist = query.getlist('type')
            if len(evalstr) == 0:
                evalstr = '( Q(img__endswith=typelist[0])'
            else: evalstr += ' & ( Q(img__endswith=typelist[0])'
            for i in range(1, len(typelist)):
                evalstr += ' | Q(img__endswith=typelist[{}])'.format(str(i))
            evalstr += ' )'

        return models.Kitty.objects.filter(eval(evalstr)).order_by('?')


        


def PickCatto(request):
    pks =  models.Kitty.objects.values_list('pk', flat=True)
    pk = random.choice(pks)
    return redirect(reverse('kitties')+r'catto/{}/'.format(str(pk)))