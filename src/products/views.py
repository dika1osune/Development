from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#a place that handles my various webpages

def home_view():
        return HttpResponse('<h1> this is my turf, I am what the word says I am</h1>')
