# catto/urls.py
from django.urls import path
from .views import KittyList, KittyCat, PickCatto, SearchKittyCat

urlpatterns = [
    path('', KittyList.as_view(), name='kitties'),
    path('catto/<int:pk>/', KittyCat.as_view(), name='catto'),
    path('catto/random/', PickCatto),
    path('catto/search/', SearchKittyCat.as_view(), name='search')
]
