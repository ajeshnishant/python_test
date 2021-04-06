# from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from user.permissions import IsAdminUser
from .serializer import SongSerializer , PodcastSerializer, AudiobookSerializer
from .models import Song, Audiobook, Podcast
# Create your views here.



class SongViewSet(ModelViewSet):

    queryset = Song.objects.all().order_by('id')
    serializer_class = SongSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = '__all__'
    # pagination_class = PageNumberPagination
    #
    # def get_permissions(self):
    #     permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]

class PodcastViewSet(ModelViewSet):

    queryset = Podcast.objects.all().order_by('id')
    serializer_class = PodcastSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = '__all__'
    # pagination_class = PageNumberPagination
    #
    # def get_permissions(self):
    #     permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]

class AudiobookViewSet(ModelViewSet):

    queryset = Audiobook.objects.all().order_by('id')
    serializer_class = AudiobookSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = '__all__'
    # pagination_class = PageNumberPagination
    #
    # def get_permissions(self):
    #     permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]