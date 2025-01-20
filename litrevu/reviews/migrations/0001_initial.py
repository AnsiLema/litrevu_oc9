# Generated by Django 5.1.4 on 2025-01-16 11:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('text', models.TextField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('Author', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('BIOGRAPHY', 'Biography'), ('DRAMA', 'Drama'), ('SCI_FI', 'Sci Fi'), ('ROMANCE', 'Romance'), ('THRILLER', 'Thriller')], max_length=10)),
            ],
        ),
    ]
