# Django REST Framework
from rest_framework import serializers

# Serializers
from genres.serializers import GenresModelSerializer
from artis.serializers import ArtisModelSerializer

# Model
from songs.models import Songs


class SongsModelSerializer(serializers.ModelSerializer):
    """Songs Model Serializer"""
    genres = GenresModelSerializer(many=True)
    artis = ArtisModelSerializer()

    class Meta:
        """Meta class."""

        model = Songs
        fields = (
            'pk',
            'name',
            'kind',
            'release_date',
            'url',
            'genres',
            'artis'
        )


class SongsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=55)
    # artis = models.ForeignKey(Artis, on_delete=models.CASCADE)
    # genres = models.ManyToManyField(Genres, related_name='songs_genres')
    kind = serializers.CharField(max_length=255)
    release_date = serializers.DateTimeField()
    url = serializers.URLField()

    def create(self, data):
        exp = Songs.objects.create(**data)
        return exp
