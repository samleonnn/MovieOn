from django.db import models

class Country(models.Model):
    country = models.CharField(max_length=200)

    class Meta:
        app_label = 'MovieOn'

    def __str__(self):
        return self.country