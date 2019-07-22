from django.http import HttpResponse
from django.shortcuts import render

# from .forms import ProductForm
# from .models import Product

# Create your views here.
#a place that handles my various webpages

def home_view(request, *args, **kwargs):
        print(request.user)
        return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
        return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
        my_context = {
                "my_text"       : "This is about us at Cognideck",
                "my_address"    : "24, Ibrahim Onashokun Street, Gbagada, Lagos.",
                "my_list"       : [123, 23243, 34994, 67, 433],
        }
        return render(request, "about.html", my_context)

def imagine_view(request, *args, **kwargs):
        return render(request, "imagine.html", {})

def social_view(request, *args, **kwargs):
        return render(request, "social.html", {})



