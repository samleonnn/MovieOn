from django.db import models
from django.contrib.auth.models import User
from MovieOn.models.movie import Movie

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'MovieOn'

    def __str__(self):
        return '%s - %s' % (self.movie.title, self.user.username)