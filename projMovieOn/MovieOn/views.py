from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from MovieOn.models import Movie, Director, Genre
from MovieOn.forms import MovieForm, DirectorForm, GenreForm

def index(request):
    # get all info here including authors, books, and genres
    num_movies = Movie.objects.all().count()
    num_directors = Director.objects.all().count()
    num_genres = Genre.objects.all().count()
    context = {
        'num_movies': num_movies,
        'num_directors': num_directors,
        'num_genres': num_genres,
    }
    return render(request, 'index.html', context=context)

def list_movies(request):
    # get all authors and add to context dictionary
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }

    return render(request, 'movies.html', context=context)

def list_directors(request):
    # get all authors and add to context dictionary
    directors = Director.objects.all()
    context = {
        'directors': directors,
    }

    return render(request, 'directors.html', context=context)

def list_genres(request):
    genres = Genre.objects.all()
    context = {
        'genres': genres,
    }
    return render(request, 'genres.html', context=context)

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('movies'))
    else:
        form = MovieForm()

    context = {
        'form': form
    }
    return render(request, 'movie_form.html', context=context)


def edit_movie(request, movie_id):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=movie_id)
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('movies'))
    else:
        movie = Movie.objects.get(pk=movie_id)
        fields = model_to_dict(movie)
        form = MovieForm(initial=fields, instance=movie)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'movie_form.html', context=context)

def add_director(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('directors'))
    else:
        form = DirectorForm()

    context = {
        'form': form
    }
    return render(request, 'director_form.html', context=context)


def edit_director(request, director_id):
    if request.method == 'POST':
        director = Director.objects.get(pk=director_id)
        form = DirectorForm(request.POST, instance=director)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('directors'))
    else:
        director = Director.objects.get(pk=director_id)
        fields = model_to_dict(director)
        form = DirectorForm(initial=fields, instance=director)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'director_form.html', context=context)

def delete_director(request, director_id):
    director = Director.objects.get(pk=director_id)
    if request.method == 'POST':
        director.delete()
        return HttpResponseRedirect(reverse('directors'))
    context = {
        'director': director
    }
    return render(request, 'director_delete_form.html', context=context)

def add_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('genres'))
    else:
        form = GenreForm()

    context = {
        'form': form
    }
    return render(request, 'genre_form.html', context=context)

def edit_genre(request, genre_id):
    if request.method == 'POST':
        genre = Genre.objects.get(pk=genre_id)
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('genres'))
    else:
        genre = Genre.objects.get(pk=genre_id)
        fields = model_to_dict(genre)
        form = GenreForm(initial=fields, instance=genre)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'genre_form.html', context=context)

def delete_genre(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    if request.method == 'POST':
        genre.delete()
        return HttpResponseRedirect(reverse('genres'))
    context = {
        'genre': genre,
    }
    return render(request, 'genre_delete_form.html', context=context)