from django.contrib import admin
from .models import Category, Article, Course, Event, QuranQuote, Comment, SavedContent

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    search_fields = ('name',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published', 'created_at')
    list_filter = ('category', 'published', 'created_at')
    list_editable = ('published',)
    search_fields = ('title', 'author', 'content')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'video_url', 'published', 'created_at')
    list_filter = ('category', 'published', 'created_at')
    list_editable = ('published',)
    search_fields = ('title', 'description', 'content')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'location', 'category', 'published')
    list_filter = ('category', 'published', 'event_date')
    list_editable = ('published',)
    search_fields = ('title', 'location', 'description')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(QuranQuote)
class QuranQuoteAdmin(admin.ModelAdmin):
    list_display = ('reference', 'verse', 'created_at')
    search_fields = ('reference', 'verse')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content_type', 'object_id', 'approved', 'created_at')
    list_filter = ('approved', 'content_type', 'created_at')
    list_editable = ('approved',)
    search_fields = ('user__username', 'content')

@admin.register(SavedContent)
class SavedContentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content_type', 'object_id', 'saved_at')
    list_filter = ('content_type', 'saved_at')
    search_fields = ('user__username', 'content_type')