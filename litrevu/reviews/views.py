from django.shortcuts import render
from django.http import HttpResponse
from reviews.models import Review

def hello(request):
    reviews = Review.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes groupes préférés sont :<p>
        <ul>
            <li>{reviews[0].name}</li>
            <li>{reviews[1].name}</li>
            <li>{reviews[2].name}</li>
            <li>{reviews[3].name}</li>
        </ul>
""")

def about(request):
    return HttpResponse("<h1>À propos</h1> <p>Nous adorons LITRevu !</p>")

def reviews(request):
    return HttpResponse("<h1>Reviews</h1> <p>Voici nos avis !</p>")

def contact(request):
    return HttpResponse("<h1>Contact</h1> <p>Contactez-nous !</p>")