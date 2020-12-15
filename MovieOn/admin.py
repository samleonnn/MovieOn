from django.contrib import admin
from MovieOn.models import movie, genre, director, age_rate, cast, country, imdb

admin.site.register(movie.Movie)
admin.site.register(genre.Genre)
admin.site.register(director.Director)
admin.site.register(age_rate.Age_rate)
admin.site.register(cast.Cast)
admin.site.register(country.Country)
admin.site.register(imdb.iMDB)
