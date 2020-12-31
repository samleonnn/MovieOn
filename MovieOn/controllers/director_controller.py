from django.shortcuts import render
from MovieOn.models.director import Director
from MovieOn.models.genre import Genre
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from MovieOn.forms import DirectorForm

def index(request):
    genre_data = Genre.objects.all()
    directors = Director.objects.all()
    context = {
        'directors': directors,
        'genre_data': genre_data,
    }

    return render(request, 'director/index.html', context=context)