from django.urls import path
from .views import Coin, Dice, Random


urlpatterns = [
    path('coin/<int:n>', Coin.as_view()),
    path('dice/<int:n>', Dice.as_view()),
    path('random/<int:n>', Random.as_view()),
]
