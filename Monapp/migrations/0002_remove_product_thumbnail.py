# Generated by Django 4.0.4 on 2022-04-18 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='thumbnail',
        ),
    ]
