# Generated by Django 3.2.19 on 2023-05-16 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
