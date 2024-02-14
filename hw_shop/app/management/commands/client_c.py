from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from app.models import Client
from random import randint


class Command(BaseCommand):
    help = "Create 'n' clients"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='client count')

    def handle(self, *args, **kwargs):
        for i in range(kwargs['count']):
            Client.objects.create(name=f'Name_{i}',
                email=f'email{i}@yandex.ru',
                phone=f'89001234{randint(100,999)}',
                address=' '.join(lorem_ipsum.words(5, common=False)))
        self.stdout.write(f'Добавлено {kwargs["count"]} клиентов')
