"""Experience URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from songs import views

router = DefaultRouter()
router.register(r'songs', views.SongsViewSet, basename='songs')

urlpatterns = [
    path('', include(router.urls))
]