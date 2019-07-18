from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#a place that handles my various webpages

def home_view(request, *args, **kwargs):
        print(request.user)
        return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
        return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
        return render(request, "about.html", {})

def imagine_view(request, *args, **kwargs):
        return render(request, "imagine.html", {})

def social_view(request, *args, **kwargs):
        return render(request, "social.html", {})
