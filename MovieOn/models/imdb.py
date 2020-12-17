from django.db import models

class IMDBID(models.Model):
    imdbid = models.CharField(max_length=200)

    class Meta:
        app_label = 'MovieOn'

    def __str__(self):
        return f'{self.imdbid}'