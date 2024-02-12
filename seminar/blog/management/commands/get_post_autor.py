from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from random import choice, randint
from blog.models import Autor, Post


class Command(BaseCommand):
    help = "Search all posts by autor."
    def add_arguments(self, parser):
        parser.add_argument('author', type=str, help='Author name')

    def handle(self, *args, **kwargs):
        autor_name = kwargs['author']
        posts = Post.objects.filter(autor__firstname__icontains=autor_name)

        for i in posts:
            self.stdout.write(str(i))
