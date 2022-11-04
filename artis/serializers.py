# Django REST Framework
from rest_framework import serializers
# Model
from artis.models import Artis


class ArtisModelSerializer(serializers.ModelSerializer):
    """Genres Model Serializer"""

    class Meta:
        """Meta class."""

        model = Artis
        fields = (
            'pk',
            'name',
            'url',
            'artist_id',
            'work_url_100',

        )
