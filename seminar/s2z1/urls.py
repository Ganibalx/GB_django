from django.urls import path
from .views import coin, stat


urlpatterns = [
    path('', coin),
    path('stat/<int:n>', stat)
]
