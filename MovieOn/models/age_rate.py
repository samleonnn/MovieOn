from django.db import models

class Age_rate(models.Model):
    rated = models.CharField(max_length=200)

    class Meta:
        app_label = 'MovieOn'

    def __str__(self):
        return f'{self.rated}'