from django.db import models

# Create your models here.
class VideoMetaData(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DurationField(null=True, blank=True)

    def __str__(self):
        return self.title

class VideoPath(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.OneToOneField(VideoMetaData, on_delete=models.CASCADE)
    folder_path = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title.title


