# Generated by Django 5.1.4 on 2025-01-18 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reviews.review'),
        ),
    ]
