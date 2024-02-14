from django.db import models


class Coin(models.Model):
    side = models.CharField(max_length=5)
    timestamp = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_static(n):
        all = Coin.objects.order_by('-timestamp')[:n]
        result = {'Орел': 0, 'Решка': 0}
        for i in all:
            if i.side == 'Орел':
                result['Орел'] += 1
            else:
                result['Решка'] += 1
        return result
