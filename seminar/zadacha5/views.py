from django.shortcuts import render
from django.http import HttpResponse
from random import choice, randint
import logging


logger = logging.getLogger(__name__)


def dec_logger(func):
    def wrapper(*args, **kwargs):
        logger.info(f'Вызвана функция {func.__name__}')
        return func(*args, **kwargs)
    return wrapper


@dec_logger
def coin(request):
    return HttpResponse(choice(['Орел', 'Решка']))


@dec_logger
def dice(request):
    return HttpResponse(f"В этот раз, на игральном кубике выпало {randint(1, 6)}")


@dec_logger
def random(request):
    return HttpResponse(randint(0, 100))
