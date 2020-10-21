from django.db import models

class Genre(models.Model):
    genre = models.CharField(max_length=200)

    def __str__(self):
        return self.genre

class Director(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    DoB = models.DateField()

    def __str__(self):
        return f'{self.First_Name} {self.Last_Name}'

class Movie(models.Model):
    title = models.CharField(max_length = 200)
    genre = models.ManyToManyField(Genre)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    datepublish = models.DateField()
    synopsis = models.TextField("Synopsis", null=True, blank=True)
    review = models.TextField("Review", null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.title


    
