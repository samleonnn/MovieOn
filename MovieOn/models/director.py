from django.db import models

class Director(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    DoB = models.DateField()
    photo = models.URLField(null=True)

    class Meta:
        app_label = 'MovieOn'

    def __str__(self):
        return f'{self.First_Name} {self.Last_Name}'