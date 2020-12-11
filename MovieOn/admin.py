from django.contrib import admin
from MovieOn.models import movie, genre, director

admin.site.register(movie.Movie)
admin.site.register(genre.Genre)
admin.site.register(director.Director)
