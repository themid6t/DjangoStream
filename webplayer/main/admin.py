from django.contrib import admin

# Register your models here.
from .models import VideoMetaData, VideoPath

admin.site.register(VideoMetaData)
admin.site.register(VideoPath)