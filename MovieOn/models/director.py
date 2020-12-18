from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)
    DoB = models.DateField(null=True)
    photo = models.URLField(null=True)

    class Meta:
        app_label = 'MovieOn'

    def __str__(self):
        return f'{self.name}'