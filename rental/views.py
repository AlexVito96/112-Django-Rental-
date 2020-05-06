from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Model View Controller/ python3 manage.py runserver/ HTML/CSS/JAVASCRIPT

# defining an endpoint
def index(request):
    return HttpResponse("Hello World")

# about send your name
def about(request):
    return HttpResponse("Alex Vito")

def soon(request):
    return HttpResponse("Page comning soon, stay in touch :) ")