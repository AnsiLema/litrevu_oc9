from django.db import models

class Review(models.Model):
    name = models.fields.CharField(max_length=100)
