from django.shortcuts import render, get_object_or_404
from MovieOn.models.genre import Genre
from MovieOn.models.movie import Movie
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from MovieOn.forms import GenreForm

def index(request, genre_slug):
    genre = get_object_or_404(Genre, slug=genre_slug)
    movie_data = Movie.objects.filter(genre=genre)
    context = {
        'genre': genre,
        'movie_data': movie_data,
    }

    return render(request, 'genre/index.html', context=context)
