# Generated by Django 5.1.4 on 2025-01-16 15:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_user_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
