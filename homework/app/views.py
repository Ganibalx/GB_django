from django.shortcuts import render
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)


def dec_logger(func):
    def wrapper(*args, **kwargs):
        logger.info(f'отбработала функция {func.__name__}')
        return func(*args, **kwargs)
    return wrapper


@dec_logger
def index(request):
    return HttpResponse('<div style="display: flex;align-items: center;margin-top: 20px;gap: 60px;flex-direction: column;"><h1>Привет,'
                        ' это главная страница!</h1><a href="about">О себе'
                        '</a><p>Тут какое-то описание, но писать лень</p><div>')


@dec_logger
def about(request):
    return HttpResponse('<div style="display: flex;align-items: center;margin-top: 20px;gap: 60px;flex-direction: column;"><h1>Меня зовут Сергей, я изучаю django'
                        '</h1><a href="http://127.0.0.1:8000">Назад'
                        '</a><p>Тут какое-то описание, но писать лень</p><div>')
