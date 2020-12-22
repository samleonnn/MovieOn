from django.shortcuts import render
from MovieOn.models.genre import Genre

def index(request):
    genre_data = Genre.objects.all()
    context = {
        'genre_data': genre_data,
    }

    return render(request, 'index.html', context=context)