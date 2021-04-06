from rest_framework.serializers import ModelSerializer
from .models import Song, Audiobook, Podcast


class SongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        # depth = 1


class AudiobookSerializer(ModelSerializer):
    class Meta:
        model = Audiobook
        fields = '__all__'
        # depth = 1


class PodcastSerializer(ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'
        # depth = 1