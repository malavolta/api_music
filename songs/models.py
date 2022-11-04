from django.db import models
from artis.models import Artis
from genres.models import Genres


# Create your models here.

class Songs(models.Model):
    name = models.CharField(max_length=255)
    artis = models.ForeignKey(Artis, related_name='artis', on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genres, related_name='genres')
    kind = models.CharField(max_length=255)
    release_date = models.DateTimeField(auto_now=False)
    url = models.URLField(null=True)

    def __str__(self):
        return self.name