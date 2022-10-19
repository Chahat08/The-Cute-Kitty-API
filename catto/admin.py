from django.contrib import admin
from . import models


class KittyAdmin(admin.ModelAdmin): 
    list_display = ('name', 'img') 

admin.site.register(models.Kitty, KittyAdmin)
