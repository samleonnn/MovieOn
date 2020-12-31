from django.shortcuts import render
import requests
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.utils.text import slugify
from django.contrib.auth.models import User

from MovieOn.models.movie import Movie
from MovieOn.models.cast import Cast
from MovieOn.models.director import Director
from MovieOn.models.genre import Genre
from MovieOn.models.ratings import Rating
from MovieOn.models.comment import Comment
from MovieOn.models.imdb import IMDB

from MovieOn.forms import MovieForm, CommentForm

def index(request):
    if request.method == 'POST':
        req = request.POST.dict()
        query = req['q']
        url = 'http://www.omdbapi.com/?apikey=df50edc8&s=' + query
        response = requests.get(url)
        movie_data = response.json()

        context = {
            'query': query,
            'movie_data': movie_data,
            'page_number': 1,
        }
        
        template = loader.get_template('movie/index.html')

        return HttpResponse(template.render(context, request))

    return render(request, 'index.html')

def pagination(request, query, page_number):
    page_number = int(page_number) + 1
    url = 'http://www.omdbapi.com/?apikey=df50edc8&s=' + query + '&page=' + str(page_number)
    response = requests.get(url)
    movie_data = response.json()

    context = {
        'query': query,
        'movie_data': movie_data,
        'page_number': page_number,
    }

    template = loader.get_template('movie/index.html')

    return HttpResponse(template.render(context, request))

def movie_details(request, imdb_id):
    if Movie.objects.filter(imdbID=imdb_id).exists():
        movie_data = Movie.objects.get(imdbID=imdb_id)
        user = request.user
        ourDB = True
        comments = Comment.objects.filter(movie=movie_data)

        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.movie = movie_data
                comment.user = user
                comment.save()
                return HttpResponseRedirect(request.path_info)
        else:
            form = CommentForm()
    else:
        url = 'http://www.omdbapi.com/?apikey=df50edc8&i=' + imdb_id
        response = requests.get(url)
        movie_data = response.json()
        comments = ''
        form = ''

        cast_obj = []
        director_obj = []
        genre_obj = []
        ratings_obj = []

        cast_list = [x.strip() for x in movie_data['Actors'].split(',')]
        for cast in cast_list:
            c, created = Cast.objects.get_or_create(name=cast)
            cast_obj.append(c)

        director_obj, created = Director.objects.get_or_create(name=movie_data['Director'])

        genre_list = list(movie_data['Genre'].replace(" ", "").split(','))
        for genre in genre_list:
            genre_slug = slugify(genre)
            g, created = Genre.objects.get_or_create(genre=genre, slug=genre_slug)
            genre_obj.append(g)

        for ratings in movie_data['Ratings']:
            r, created = Rating.objects.get_or_create(source=ratings['Source'], rating=ratings['Value'])
            ratings_obj.append(r)

        m, created = Movie.objects.get_or_create(
            title = movie_data['Title'],
            year = movie_data['Year'],
            rated = movie_data['Rated'],
            datepublish = movie_data['Released'],
            runtime = movie_data['Runtime'],
            director = director_obj,
            writer = movie_data['Writer'],
            synopsis = movie_data['Plot'],
            country = movie_data['Country'],
            poster = movie_data['Poster'],
            imdbID = movie_data['imdbID'],
            type = movie_data['Type'],
        )

        m.cast.set(cast_obj)
        m.genre.set(genre_obj)
        m.ratings.set(ratings_obj)

        n, created = IMDB.objects.get_or_create(imdb_id=movie_data['imdbID'], movie=m)
        
        m.save()
        ourDB = False

    context = {
        'movie_data': movie_data,
        'ourDB': ourDB,
        'comments': comments,
        'form': form,
    }

    template = loader.get_template('movie/movie_details.html')

    return HttpResponse(template.render(context, request))

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
    return render(request, 'movie/movie_form.html', context=context)

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
    return render(request, 'movie/movie_form.html', context=context)
