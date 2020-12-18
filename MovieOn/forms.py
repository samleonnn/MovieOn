from django.forms import ModelForm
from django.core.exceptions import ValidationError
from MovieOn.models.movie import Movie
from MovieOn.models.director import Director
from MovieOn.models.genre import Genre

class MovieForm(ModelForm):
    class Meta:
        model = Movie  # model to use in form
        # list of fields to be displayed
        fields = ['title', 'year', 'rated', 'datepublish', 'runtime', 'genre', 'director', 'writer','cast', 'synopsis', 'country', 'poster', 'ratings', 'imdbID','type']


class DirectorForm(ModelForm):
    class Meta:
        model = Director  # model to use in form
        # list of fields to be displayed
        fields = ['name', 'DoB']

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ['genre']