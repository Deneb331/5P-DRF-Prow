# Generated by Django 3.2.19 on 2023-05-15 18:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cards', '0002_auto_20230515_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='member_models', to=settings.AUTH_USER_MODEL),
        ),
    ]
