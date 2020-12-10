from django.forms import ModelForm
from django.core.exceptions import ValidationError
from MovieOn.models import Movie, Director, Genre

class MovieForm(ModelForm):
    class Meta:
        model = Movie  # model to use in form
        # list of fields to be displayed
        fields = ['title', 'genre', 'director', 'datepublish', 'synopsis', 'review', 'rating']


class DirectorForm(ModelForm):
    class Meta:
        model = Director  # model to use in form
        # list of fields to be displayed
        fields = ['First_Name', 'Last_Name', 'DoB']

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ['genre']