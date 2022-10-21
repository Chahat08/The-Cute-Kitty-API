import random
from django.db import models

# Create your models here.

class Kitty(models.Model):
    name = models.IntegerField(primary_key=True, blank=True, default=random.randint(1,1000))
    img = models.ImageField(upload_to="cats/", blank=True)
    tags = models.TextField(blank=True, default="cute")

    def __str__(self):
        return str(self.name)

