# Generated by Django 5.0.3 on 2024-03-15 16:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('postcode', models.CharField(max_length=10)),
                ('house_number', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=200)),
                ('apartment_number', models.CharField(blank=True, max_length=10, null=True)),
                ('place_id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lng', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('full_name', models.CharField(max_length=60)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.house')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=6)),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='item_images')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
