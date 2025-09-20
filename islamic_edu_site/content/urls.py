from django.urls import path
from core import views as core_views
from . import views



urlpatterns = [
    # Home page - root URL
    path('', views.home, name='home'),
    
    # Articles
    path('articles/', views.ArticleListView.as_view(), name='article_list'),
    path('articles/<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail_slug'),
    
    # Courses
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('courses/<slug:slug>/', views.CourseDetailView.as_view(), name='course_detail'),
    
    # Events
    path('events/', views.EventListView.as_view(), name='event_list'),
    path('events/<slug:slug>/', views.EventDetailView.as_view(), name='event_detail'),
    
    # Categories
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail_slug'),
    
    # Quran Quotes
    path('quran-quotes/', views.QuranQuoteListView.as_view(), name='quran_quote_list'),
    
    # Search
    path('search/', views.search, name='search'),
    path("faq/", core_views.faq, name="faq"),
    path("about/", core_views.about, name="about"),
    path("contact/", core_views.contact, name="contact"),
]