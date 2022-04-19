# Generated by Django 3.2.8 on 2022-04-19 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wb', '0004_auto_20220419_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apikey',
            name='api',
            field=models.CharField(max_length=200, verbose_name='Ключ API (x64)'),
        ),
        migrations.AlterField(
            model_name='apikey',
            name='new_api',
            field=models.CharField(default='', max_length=400, verbose_name='Ключ нового API (JWT)'),
        ),
    ]