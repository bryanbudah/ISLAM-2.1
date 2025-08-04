from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_url = models.URLField(blank=True)
    pdf = models.FileField(upload_to='courses/pdfs/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    rsvp_link = models.URLField(blank=True)