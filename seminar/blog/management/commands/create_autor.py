from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from blog.models import Autor


class Command(BaseCommand):
    help = "Create autor."
    def handle(self, *args, **kwargs):
        for i in range(10):
            Autor.objects.create(firstname=f'Name{i}',
                lastname=f'Lastname{i}',
                email=f'mail{i}@yandex.ru',
                bio=' '.join(lorem_ipsum.paragraphs(5)),
                birthday='2000-01-12')
        self.stdout.write(f'Автор создан')
