# Generated by Django 5.0.2 on 2024-02-25 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=True, max_length=25)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(blank=True, max_length=1024, null=True)),
                ('emp_code', models.CharField(max_length=10, null=True, unique=True)),
                ('state', models.CharField(max_length=30, null=True)),
                ('city', models.CharField(max_length=30, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('registered_on', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
