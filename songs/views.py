# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsStandardUser

# Serializers
from songs.serializers import SongsModelSerializer, SongsSerializer

# Models
from songs.models import Songs
from django.db.models import Q


class SongsViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = SongsModelSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsStandardUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        condition = Q()
        name_artis = self.request.query_params.get('name_artis')

        if name_artis is not None:
            condition = Q(artis__name__exact=name_artis)

        queryset = Songs.objects.filter(condition)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = SongsSerializer(data=request.data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        exp = serializer.save()
        data = SongsModelSerializer(exp).data


        return Response(data, status=status.HTTP_201_CREATED)
