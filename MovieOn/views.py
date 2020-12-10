from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from MovieOn.models import Movie, Director, Genre
from MovieOn.forms import MovieForm, DirectorForm, GenreForm


def index(request):
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
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }

    return render(request, 'movies.html', context=context)

def list_directors(request):
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

@login_required
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('movies'))
    else:
        form = MovieForm()

    context = {
        'form': form
    }
    return render(request, 'movie_form.html', context=context)

@login_required
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

@login_required
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

@login_required
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

@login_required
def delete_director(request, director_id):
    director = Director.objects.get(pk=director_id)
    if request.method == 'POST':
        director.delete()
        return HttpResponseRedirect(reverse('directors'))
    context = {
        'director': director
    }
    return render(request, 'director_delete_form.html', context=context)

@login_required
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

@login_required
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

@login_required
def delete_genre(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    if request.method == 'POST':
        genre.delete()
        return HttpResponseRedirect(reverse('genres'))
    context = {
        'genre': genre,
    }
    return render(request, 'genre_delete_form.html', context=context)

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def register(request):
    msg = ''
    if request.method == 'POST':
        req = request.POST.dict()
        username = req['username']
        password = req['password']
        email = req['email']
        try:
            user = User.objects.get(username=username)
            msg = 'Username or E-Mail is already registered'
        except User.DoesNotExist:
            user = User.objects.create_user(username, email, password)
            user.save()
            msg = ''
            html_message = render_to_string('regis_email.html', {'context': 'values'}, username)
            send_mail(
                'Welcome to MovieOn journey!',
                'You are now a member of MovieOn',
                settings.EMAIL_HOST_USER,
                [email],
                html_message = html_message,
                fail_silently=True,
            )
        return HttpResponseRedirect('accounts/login?next=/')
    data = {
        'user_exists_error': msg,
    }
    return render(request, 'registration.html', data)
