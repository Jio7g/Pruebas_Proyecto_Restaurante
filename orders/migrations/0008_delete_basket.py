# Generated by Django 3.0.7 on 2020-06-09 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_extras_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Basket',
        ),
    ]
