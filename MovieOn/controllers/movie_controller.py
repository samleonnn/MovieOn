from django.shortcuts import render
import requests
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.utils.text import slugify

from MovieOn.models.movie import Movie
from MovieOn.models.age_rate import Age_rate
from MovieOn.models.cast import Cast
from MovieOn.models.country import Country
from MovieOn.models.director import Director
from MovieOn.models.genre import Genre
from MovieOn.models.imdb import IMDBID
from MovieOn.models.ratings import Rating

from MovieOn.forms import MovieForm

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
    url = 'http://www.omdbapi.com/?apikey=df50edc8&s=' + query + '&page=' + str(page_number)
    response = requests.get(url)
    movie_data = response.json()
    page_number = int(page_number) + 1

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
        ourDB = True
    else:
        url = 'http://www.omdbapi.com/?apikey=df50edc8&i=' + imdb_id
        response = requests.get(url)
        movie_data = response.json()

        rated_obj = []
        cast_obj = []
        country_obj = []
        director_obj = []
        genre_obj = []
        imdb_obj = []
        ratings_obj = []

        ra,created = Age_rate.objects.get_or_create(rated=movie_data['Rated'])
        rated_obj.append(ra)

        cast_list = [x.strip() for x in movie_data['Actors'].split(',')]
        for cast in cast_list:
            c, created = Cast.objects.get_or_create(name=cast)
            cast_obj.append(c)

        co, created = Country.objects.get_or_create(country=movie_data['Country'])
        country_obj.append(co)

        di, created = Director.objects.get_or_create(name=movie_data['Director'])
        director_obj.append(di)

        genre_list = list(movie_data['Genre'].replace(" ", "").split(','))
        for genre in genre_list:
            genre_slug = slugify(genre)
            g, created = Genre.objects.get_or_create(genre=genre, slug=genre_slug)
            genre_obj.append(g)

        i, created = IMDBID.objects.get_or_create(imdbid=movie_data['imdbID'])
        imdb_obj.append(i)

        for ratings in movie_data['Ratings']:
            r, created = Rating.objects.get_or_create(source=ratings['Source'], rating=ratings['Value'])
            ratings_obj.append(r)

        if movie_data['Type'] == 'movie':
            m, created = Movie.objects.get_or_create(
                title = movie_data['Title'],
                year = movie_data['Year'],
                datepublish = movie_data['Released'],
                runtime = movie_data['Runtime'],
                writer = movie_data['Writer'],
                synopsis = movie_data['Plot'],
                poster = movie_data['Poster'],
                type = movie_data['Type'],
            )

            m.rated.set(rated_obj)
            m.cast.set(cast_obj)
            m.country.set(country_obj)
            m.director.set(director_obj)
            m.genre.set(genre_obj)
            m.imdbID.set(imdb_obj)
            m.ratings.set(ratings_obj)
        else:
            m, created = Movie.objects.get_or_create(
                title = movie_data['Title'],
                year = movie_data['Year'],
                datepublish = movie_data['Released'],
                runtime = movie_data['Runtime'],
                writer = movie_data['Writer'],
                synopsis = movie_data['Plot'],
                poster = movie_data['Poster'],
                type = movie_data['Type'],
                totalseasons = movie_data['totalSeasons']
            )

            m.rated.set(rated_obj)
            m.cast.set(cast_obj)
            m.country.set(country_obj)
            m.director.set(director_obj)
            m.genre.set(genre_obj)
            m.imdbID.set(imdb_obj)
            m.ratings.set(ratings_obj)

        for cast in cast_obj:
            cast.movies.add(m)
            cast.save()
        
        m.save()
        ourDB = False

    context = {
        'movie_data': movie_data,
        'ourDB': ourDB,
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
