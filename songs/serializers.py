# Django REST Framework
from rest_framework import serializers

# Serializers
from genres.serializers import GenresModelSerializer
from artis.serializers import ArtisModelSerializer

# Model
from songs.models import Songs
from genres.models import Genres


class SongsModelSerializer(serializers.ModelSerializer):
    """Songs Model Serializer"""
    genres = GenresModelSerializer(many=True, read_only=False)
    artis = ArtisModelSerializer(read_only=False)

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
    artis_id = serializers.IntegerField()
    genres = serializers.ListField()
    kind = serializers.CharField(max_length=255)
    release_date = serializers.DateTimeField()
    url = serializers.URLField()

    def create(self, data):
        song = Songs.objects.create(name=data['name'], artis_id=data['artis_id'], kind=data['kind'],
                                    release_date=data['release_date'], url=data['url'])

        for genre in data["genres"]:
            print(str(genre["id"]))
            genre_obj = Genres.objects.get(id=genre["id"])
            song.genres.add(genre_obj)

        return song
