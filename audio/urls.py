from rest_framework.routers import DefaultRouter
from .views import SongViewSet, AudiobookViewSet, PodcastViewSet
from django.urls import include, path
router = DefaultRouter()
router.register(r'song', SongViewSet)
router.register(r'audiobook', AudiobookViewSet)
router.register(r'podcast', PodcastViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]