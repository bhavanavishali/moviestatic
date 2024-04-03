from django.db import models

# Create your models here.
class Movies(models.Model):
    movie = models.CharField(max_length=100)
    des = models.TextField()
    year = models.IntegerField()
    image = models.ImageField()

    def __str__(self) -> str:
        return self.movie
