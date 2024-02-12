from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from random import choice
from zadacha5.views import dec_logger
from .models import Coin


@dec_logger
def coin(request):
    result = choice(['Орел', 'Решка'])
    Coin.objects.create(side=result)
    return HttpResponse(result)


@dec_logger
def stat(request, n):
    return JsonResponse(Coin.get_static(n), json_dumps_params={'ensure_ascii': False})
