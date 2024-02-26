from django.contrib import admin
from .models import Client, Product, Order


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'register']
    ordering = ['register']
    readonly_fields = ['register']
    fieldsets = [('Имя', {'fields': ['name']}),
                 ('Контактная информация', {'fields': ['email', 'phone', 'address']}),
                 ('Регистрация', {'fields': ['register']})]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'count', 'data_add']
    ordering = ['data_add']
    readonly_fields = ['data_add', 'count']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ordering = ['order_data']
    readonly_fields = ['order_data', 'client', 'order_price']
