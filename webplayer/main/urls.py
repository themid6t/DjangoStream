from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/', views.movies, name='movies'),
    path('watch/<int:movie_id>/', views.watch, name='watch'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)