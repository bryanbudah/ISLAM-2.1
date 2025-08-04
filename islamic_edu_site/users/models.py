from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any additional fields here
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)  # ✅ Added
    website = models.URLField(blank=True)  # ✅ Added

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Additional profile-specific fields can go here
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
