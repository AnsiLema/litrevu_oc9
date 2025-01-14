from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1>Hello Django!</h1>")

def about(request):
    return HttpResponse("<h1>À propos</h1> <p>Nous adorons LITRevu !</p>")

def reviews(request):
    return HttpResponse("<h1>Reviews</h1> <p>Voici nos avis !</p>")

def contact(request):
    return HttpResponse("<h1>Contact</h1> <p>Contactez-nous !</p>")