# Generated by Django 5.2.1 on 2025-05-27 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='genre',
            field=models.CharField(default='', max_length=30, verbose_name='Жанр'),
        ),
    ]
