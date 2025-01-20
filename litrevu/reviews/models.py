from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Review(models.Model):

    class Genre(models.TextChoices):
        BIOGRAPHY = "BIOGRAPHY"
        DRAMA = "DRAMA"
        SCI_FI = "SCI_FI"
        ROMANCE = "ROMANCE"
        THRILLER = "THRILLER"
        COMEDY = "COMEDY"

    name = models.fields.CharField(max_length=100)
    rating = models.fields.IntegerField(default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    text = models.fields.TextField(max_length=1000)
    date = models.fields.DateTimeField(auto_now_add=True)
    author = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=10)
    year_of_release = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2025)]
    )

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.fields.CharField(max_length=100)
    email = models.fields.EmailField()
    password = models.fields.CharField(max_length=50)
    review = models.ForeignKey(Review, null=True, blank=True, on_delete=models.SET_NULL)

    def __srt__(self):
        return self.username
