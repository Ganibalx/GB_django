from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from random import choice, randint
from blog.models import Autor, Post


class Command(BaseCommand):
    help = "Create post."
    def handle(self, *args, **kwargs):
        autors = Autor.objects.all()
        for i in range(10):
            Post.objects.create(title=lorem_ipsum.words(5, common=False).capitalize(),
                content='\n'.join(lorem_ipsum.paragraphs(7, common=False)),
                pub_date=f'2024-01-{randint(10,30)}',
                autor=choice(autors),
                category=choice(lorem_ipsum.WORDS).capitalize)
        self.stdout.write(f'Пост создан')
