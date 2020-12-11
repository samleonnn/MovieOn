from django.shortcuts import render
from MovieOn.models.director import Director
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from MovieOn.forms import DirectorForm

def index(request):
    directors = Director.objects.all()
    context = {
        'directors': directors,
    }

    return render(request, 'directors.html', context=context)

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