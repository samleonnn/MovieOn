from django.db import models
from MovieOn.models.genre import Genre

class Movie(models.Model):
    title = models.CharField(max_length = 200)
    genre = models.ManyToManyField(Genre)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    datepublish = models.DateField()
    synopsis = models.TextField("Synopsis", null=True, blank=True)
    review = models.TextField("Review", null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    class Meta:
        app_label = 'MovieOn'

    def __str__(self):
        return self.title