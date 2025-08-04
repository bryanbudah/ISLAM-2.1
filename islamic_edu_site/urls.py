# islamic_edu_site/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from content import views as content_views  # Import home view

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home page
    path('', content_views.home, name='home'),

    # App routes
    path('', include('content.urls')),  # Handles /articles/, /events/, /courses/, and detail pages
    path('users/', include('users.urls')),
]

# Serve static/media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
