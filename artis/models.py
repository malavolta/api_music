from django.db import models


# Create your models here.

class Artis(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(null=True)
    artist_id = models.CharField(max_length=15)
    work_url_100 = models.URLField(null=True)

    def __str__(self):
        return self.name
