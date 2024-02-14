from django.shortcuts import render
from django.views.generic import TemplateView
from random import choice, randint


class Coin(TemplateView):
    template_name = 's3/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Бросок монетки'
        result = dict()
        for i in range(kwargs['n']):
            result[i+1] = choice(['Орел', 'Решка'])
        context['result'] = result
        return context


class Dice(TemplateView):
    template_name = 's3/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'бросаем кубик'
        result = dict()
        for i in range(kwargs['n']):
            result[i+1] = randint(1, 6)
        context['result'] = result
        return context


class Random(TemplateView):
    template_name = 's3/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'рандомное число'
        result = dict()
        for i in range(kwargs['n']):
            result[i+1] = randint(0, 100)
        context['result'] = result
        return context
