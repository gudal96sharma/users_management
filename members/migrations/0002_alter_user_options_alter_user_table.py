# Generated by Django 5.0.2 on 2024-02-25 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]