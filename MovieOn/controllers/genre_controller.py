from django.shortcuts import render
from MovieOn.models.genre import Genre
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from MovieOn.forms import GenreForm

def index(request):
    genres = Genre.objects.all()
    context = {
        'genres': genres,
    }

    return render(request, 'genres.html', context=context)

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