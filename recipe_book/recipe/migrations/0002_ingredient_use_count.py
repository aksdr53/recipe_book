# Generated by Django 3.2.3 on 2024-01-28 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='use_count',
            field=models.IntegerField(default=0, verbose_name='Количество использований'),
        ),
    ]