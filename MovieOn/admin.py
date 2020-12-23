from django.contrib import admin
from MovieOn.models import movie, genre, director, cast, ratings, comment

admin.site.register(movie.Movie)
admin.site.register(genre.Genre)
admin.site.register(director.Director)
admin.site.register(cast.Cast)
admin.site.register(ratings.Rating)
admin.site.register(comment.Comment)
