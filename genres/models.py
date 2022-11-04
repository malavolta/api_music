from django.db import models


class Genres(models.Model):
    name = models.CharField(max_length=55)
    url = models.URLField(null=True)

    def __str__(self):
        return self.name
