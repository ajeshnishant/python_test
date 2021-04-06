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
    

class PodcastViewSet(ModelViewSet):

    queryset = Podcast.objects.all().order_by('id')
    serializer_class = PodcastSerializer
    

class AudiobookViewSet(ModelViewSet):

    queryset = Audiobook.objects.all().order_by('id')
    serializer_class = AudiobookSerializer
   
