from django.urls import path
from .views import Coin, Dice, Random


urlpatterns = [
    path('coin/<int:n>', Coin.as_view(), name='coin'),
    path('dice/<int:n>', Dice.as_view(), name='dice'),
    path('random/<int:n>', Random.as_view(), name='random'),
]
