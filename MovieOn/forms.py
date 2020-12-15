from django.forms import ModelForm
from django.core.exceptions import ValidationError
from MovieOn.models.movie import Movie
from MovieOn.models.director import Director
from MovieOn.models.genre import Genre

class MovieForm(ModelForm):
    class Meta:
        model = Movie  # model to use in form
        # list of fields to be displayed
        fields = ['title', 'year', 'genre', 'director', 'datepublish', 'cast', 'country', 'MPAA_ratings', 'synopsis', 'photo']


class DirectorForm(ModelForm):
    class Meta:
        model = Director  # model to use in form
        # list of fields to be displayed
        fields = ['First_Name', 'Last_Name', 'DoB']

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ['genre']