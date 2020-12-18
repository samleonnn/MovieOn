from django.db import models
from django.utils.text import slugify

class Cast(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=True, unique=True)

    class Meta:
        app_label = 'MovieOn'

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)