from django.db import models
from artis.models import Artis
from genres.models import Genres


# Create your models here.

class Songs(models.Model):
    name = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genres)
    artis = models.ForeignKey(Artis, on_delete=models.CASCADE)
    kind = models.CharField(max_length=255)
    release_date = models.DateTimeField(auto_now_add=True)
    url = models.URLField(null=True)

    def __str__(self):
        return self.name
