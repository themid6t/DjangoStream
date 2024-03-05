from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import VideoMetaData, VideoPath
import os

def home(response):
    return render(response, 'main/index.html')

def movies(response):
    movies = VideoMetaData.objects.all()
    return render(response, 'main/movie.html', {'movies': movies})

def watch(response, movie_id):
    movie_metadata = get_object_or_404(VideoMetaData, id=movie_id)
    movie = get_object_or_404(VideoPath, title=movie_metadata)
    path = os.path.join(movie.folder_path)
    print(path)

    return render(response, 'main/watch.html', {'movie': movie, 'path': path})