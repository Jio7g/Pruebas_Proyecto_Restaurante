# Generated by Django 2.0.3 on 2020-06-05 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0004_auto_20200605_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(decimal_places=2, default='00.00', max_digits=6)),
                ('pastaItems', models.ManyToManyField(blank=True, related_name='pastaBask', to='orders.Pasta')),
                ('pizItems', models.ManyToManyField(blank=True, related_name='pizBask', to='orders.PizOrder')),
                ('platItems', models.ManyToManyField(blank=True, related_name='platBask', to='orders.Platter')),
                ('saladItems', models.ManyToManyField(blank=True, related_name='saladBask', to='orders.Salad')),
                ('subItems', models.ManyToManyField(blank=True, related_name='subBask', to='orders.Sub')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
