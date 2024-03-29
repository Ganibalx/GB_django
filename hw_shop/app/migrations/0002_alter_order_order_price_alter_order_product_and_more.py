# Generated by Django 4.2.7 on 2024-02-14 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(related_name='products', to='app.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='data_add',
            field=models.DateField(auto_now=True),
        ),
    ]
