# Generated by Django 5.1.4 on 2025-01-16 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_review_year_of_release'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='Author',
            new_name='author',
        ),
    ]
