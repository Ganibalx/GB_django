from django.db import models
from django.urls import reverse


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField()
    phone = models.CharField(max_length=11, verbose_name='Телефон')
    address = models.CharField(max_length=30, verbose_name='Адрес')
    register = models.DateField(auto_now=True, verbose_name='Дата регистрации')

    def __str__(self):
        return f'Клиент {self.name}'

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    description = models.TextField(verbose_name='Описание продукта')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    count = models.IntegerField(default=1, verbose_name='Количество')
    img = models.ImageField(upload_to='products/', verbose_name='Изображение')
    data_add = models.DateField(auto_now=True, verbose_name='Дата добавления')

    def __str__(self):
        return f'Продукт{self.name}'

    def get_desc(self):
        return self.description[:20]

    def get_absolute_url(self):
        return reverse("updateproduct", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Заказчик')
    product = models.ManyToManyField(Product, verbose_name='Продукты')
    order_price = models.DecimalField(max_digits=6, decimal_places=2, default=0, verbose_name='Общая цена')
    order_data = models.DateField(auto_now=True, verbose_name='Дата заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ клиента {self.client.name}'
