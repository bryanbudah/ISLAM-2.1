from django.contrib import admin
from django.contrib import admin
from core.models import Course, Article, Event  # Import your models

# Register models to appear in Django admin
admin.site.register(Course)
admin.site.register(Article)
admin.site.register(Event)
# Register your models here.
