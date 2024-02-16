from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime, timedelta
from .models import Client, Order, Product


class OrderList(TemplateView):
    template_name = 'app/orderlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client'] = Client.objects.filter(id=context['pk']).first().name
        context['orders'] = Order.objects.filter(client_id=context['pk']).order_by('order_data').prefetch_related('product')
        for order in context['orders']:
            order.products = order.product.all()
        interval = [7, 30, 365]
        for i in interval:
            order = Order.objects.filter(client_id=context['pk'], order_data__gte=datetime.now().date() - timedelta(days=i)).order_by('order_data').prefetch_related('product')
            products = []
            for j in order:
                product = j.product.all()
                for p in product:
                    if p not in products:
                        products.append(p)
            context[f'products{i}'] = products
        return context
