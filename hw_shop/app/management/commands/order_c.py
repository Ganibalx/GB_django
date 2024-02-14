from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from app.models import Client, Order, Product
from random import randint, choice


class Command(BaseCommand):
    help = "Create 'n' orders"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='order count')

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        for i in range(kwargs['count']):
            order = Order.objects.create(client=choice(clients))
            for j in range(randint(1, 5)):
                price = round(randint(1000, 9999)/100, 2)
                order.product.create(name=choice(lorem_ipsum.WORDS),
                                description='\n'.join(lorem_ipsum.paragraphs(2, common=False)),
                                price=price,
                                count=randint(1, 10))
                order.order_price += price
            order.save()
        self.stdout.write(f'Добавлено {kwargs["count"]} заказов')
