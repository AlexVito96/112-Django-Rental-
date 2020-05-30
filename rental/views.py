from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Movie

# Create your views here.
# Model View Controller/ python3 manage.py runserver/ HTML/CSS/JAVASCRIPT

# defining an endpoint
def index(request):
    all_movies = Movie.objects.all() # read Movie table to a list
    return render(request,'index.html', { 'title': 'Movies Catalog', 'movies': all_movies })

def details(request, movie_id):
    try:
        the_movie = Movie.objects.get(id=movie_id)
        return render(request, 'details.html', {'movie': the_movie})
    except:
        return render(request, 'NotFound.html')

def catalog(request):
    return render(request, 'catalog.html')

# about send your name
def about(request):
    return render(request, 'about.html')

def soon(request):
   return render(request, 'comingSoon.html')

