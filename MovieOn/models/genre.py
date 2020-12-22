from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Genre(models.Model):
    genre = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        app_label = 'MovieOn'

    def get_absolute_url(self):
        return reverse('genres', args=[self.slug])

    def __str__(self):
        return f'{self.genre}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.genre.replace(" ", "")
            self.slug = slugify(self.genre)
        return super().save(*args, **kwargs)