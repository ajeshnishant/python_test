from django.contrib import admin

# Register your models here.
from .models import Song
from .models import Audiobook
from .models import Podcast


admin.site.register(Song)
admin.site.register(Audiobook)
admin.site.register(Podcast)