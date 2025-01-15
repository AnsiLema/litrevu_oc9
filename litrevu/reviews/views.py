from django.shortcuts import render
from django.http import HttpResponse
from reviews.models import Review

def hello(request):
     return render(request, "reviews/hello.html")

def about(request):
    return render(request, "reviews/about.html")

def reviews(request):
    reviews = Review.objects.all()
    return render(request, "reviews/review.html", {"reviews": reviews})

def contact(request):
    return render(request, "reviews/contact.html")