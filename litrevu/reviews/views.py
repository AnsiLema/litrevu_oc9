from django.shortcuts import render
from django.http import HttpResponse
from reviews.models import Review
from reviews.models import User
from reviews.forms import ContactUsForm

def user_list(request):
    user_list = User.objects.all()
    return render(request, "reviews/user_list.html", {"user_list": user_list})

def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, "reviews/user_detail.html", {"user": user})


def about(request):
    return render(request, "reviews/about.html")

def reviews(request):
    reviews = Review.objects.all()
    return render(request, "reviews/review.html", {"reviews": reviews})

def contact(request):
    form = ContactUsForm() # Add the new form
    return render(request, "reviews/contact.html", {"form": form}) # Passes form to the template