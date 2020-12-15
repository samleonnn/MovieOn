from django.db import models
from MovieOn.models.genre import Genre
from MovieOn.models.cast import Cast
from MovieOn.models.imdb import iMDB
from MovieOn.models.country import Country

class Movie(models.Model):
    title = models.CharField(max_length = 200)
    year = models.CharField(max_length = 5, null=True)
    genre = models.ManyToManyField(Genre)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    datepublish = models.CharField(max_length = 100)
    cast = models.ManyToManyField(Cast)
    country = models.ManyToManyField(Country)
    MPAA_ratings = models.ForeignKey('Age_rate', on_delete=models.SET_NULL, null=True)
    synopsis = models.TextField("Synopsis", null=True, blank=True)
    photo = models.URLField(null=True)

    class Meta:
        app_label = 'MovieOn'

    def __str__(self):
        return self.title