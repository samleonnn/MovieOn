from django.db import models
from MovieOn.models.genre import Genre
from MovieOn.models.cast import Cast
from MovieOn.models.imdb import IMDBID
from MovieOn.models.country import Country
from MovieOn.models.ratings import Rating
from MovieOn.models.age_rate import Age_rate
from MovieOn.models.director import Director

class Movie(models.Model):
    title = models.CharField(max_length = 200)
    year = models.CharField(max_length = 5)
    rated = models.ForeignKey(Age_rate, null=True, on_delete=models.SET_NULL)
    datepublish = models.CharField(max_length = 100)
    runtime = models.CharField(max_length=25)
    genre = models.ManyToManyField(Genre)
    director = models.ForeignKey(Director, null=True, on_delete=models.SET_NULL)
    writer = models.CharField(max_length=1000)
    cast = models.ManyToManyField(Cast)
    synopsis = models.CharField(max_length=1000)
    country = models.ManyToManyField(Country)
    poster = models.URLField()
    ratings = models.ManyToManyField(Rating)
    imdbID = models.OneToOneField(IMDBID, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    totalseasons = models.CharField(max_length=4)

    class Meta:
        app_label = 'MovieOn'

    def __str__(self):
        return f'{self.title}'