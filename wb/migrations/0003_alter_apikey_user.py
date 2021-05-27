# Generated by Django 3.2.3 on 2021-05-27 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wb', '0002_alter_apikey_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apikey',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
