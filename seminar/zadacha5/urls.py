from django.urls import path
from .views import coin, dice, random


urlpatterns = [
    path('coin/', coin),
    path('dice/', dice),
    path('random/', random),
]
