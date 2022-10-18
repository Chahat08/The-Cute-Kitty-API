# catto/urls.py
from django.urls import path
from .views import KittyList

urlpatterns = [
    path('', KittyList.as_view(), name='kitties'),
]
