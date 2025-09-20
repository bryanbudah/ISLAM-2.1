from django.conf import settings
from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class ContentBase(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    content = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to='content_images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if self.__class__.objects.filter(slug=self.slug).exists():
                self.slug = f"{self.slug}-{self.id or 'new'}"
        super().save(*args, **kwargs)

class Course(ContentBase):
    video_url = models.URLField(blank=True, null=True)
    video = models.FileField(upload_to="articles/videos/", blank=True, null=True)

class Article(ContentBase):
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to="articles/images/", blank=True, null=True)  # ✅ thumbnail
    video = models.FileField(upload_to="articles/videos/", blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

class Event(ContentBase):
    event_date = models.DateField()
    location = models.CharField(max_length=255)
    video = models.FileField(upload_to="articles/videos/", blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

class QuranQuote(models.Model):
    verse = models.TextField()
    reference = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reference

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=50)
    object_id = models.PositiveIntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} on {self.content_type} ({self.object_id})"

class SavedContent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=50)
    object_id = models.PositiveIntegerField()
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'content_type', 'object_id')
        ordering = ['-saved_at']

    def __str__(self):
        return f"{self.user.username} saved {self.content_type} ({self.object_id})"

