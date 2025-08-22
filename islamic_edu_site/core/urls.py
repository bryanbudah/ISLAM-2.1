from django.urls import path
from . import views
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
path('courses/', views.courses, name='courses'),

path('articles/', views.articles, name='article_list'),
path('events/', views.events, name='event_list'),
path('courses/', views.course_list, name='course_list'),