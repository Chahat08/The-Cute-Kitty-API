import random
from django.db import models

# Create your models here.

class Kitty(models.Model):
    name = models.CharField(max_length=100, blank=True, default=str(random.randint(1,1000)))
    img = models.ImageField(upload_to="cats/", blank=True)
    breed = models.CharField(max_length=100, blank=True, default="cute")

    def __str__(self):
        return self.name

