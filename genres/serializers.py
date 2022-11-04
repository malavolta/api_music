# Django REST Framework
from rest_framework import serializers
# Model
from genres.models import Genres


class GenresModelSerializer(serializers.ModelSerializer):
    """Genres Model Serializer"""

    class Meta:
        """Meta class."""

        model = Genres
        fields = (
            'pk',
            'name',
            'url',
        )


class GenresSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=55)
    url = serializers.URLField(required=False)

    def create(self, data):
        exp = Genres.objects.create(**data)
        return exp
