from rest_framework import serializers
from . import models

class KittySerializer(serializers.ModelSerializer): 
    class Meta: 
        model = models.Kitty
        fields = ('name', 'img', 'breed')