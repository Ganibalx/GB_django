from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from random import choice, randint
from blog.models import Autor, Post, Comment


class Command(BaseCommand):
    help = "Create post."
    def handle(self, *args, **kwargs):
        autors = Autor.objects.all()
        post = Post.objects.all()
        for i in range(10):
            Comment.objects.create(author=choice(autors),
                post=choice(post),
                content='\n'.join(lorem_ipsum.paragraphs(3, common=False)),
                create_date=f'2024-01-{randint(10,30)}',
                edit_date=f'2024-02-{randint(10,28)}',)
        self.stdout.write(f'Коменты созданы')
