from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=20)

class Movie(models.Model):
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    # genre = models.CharField(max_length=20)
    # score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)

class Score(models.Model):
    content = models.TextField()
    score = models.FloatField()
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)