from django.db import models

class Rating(models.Model):
    source = models.CharField(max_length=100)
    rating = models.CharField(max_length=50)

    class Meta:
        app_label = 'MovieOn'

    def __str__(self):
        return f'{self.source}'