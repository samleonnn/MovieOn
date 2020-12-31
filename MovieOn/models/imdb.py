from django.db import models
from MovieOn.models.movie import Movie

class IMDB(models.Model):
    imdb_id = models.CharField(max_length=100)
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE, null=True)

    class Meta:
        app_label = 'MovieOn'

    def __str__(self):
        return f'{self.imdb_id}'