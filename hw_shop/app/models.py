from django.db import models
from django.urls import reverse


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=30)
    register = models.DateField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    count = models.IntegerField(default=1)
    img = models.ImageField(upload_to='products/')
    data_add = models.DateField(auto_now=True)

    def get_desc(self):
        return self.description[:20]

    def get_absolute_url(self):
        return reverse("updateproduct", kwargs={"pk": self.pk})


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    order_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    order_data = models.DateField(auto_now=True)

