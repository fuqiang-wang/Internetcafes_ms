# Generated by Django 3.0.3 on 2020-06-03 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='goods_num',
            field=models.IntegerField(default=0),
        ),
    ]
