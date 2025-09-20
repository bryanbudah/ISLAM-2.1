from django.urls import path
from . import views
from core import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    

path('courses/', views.courses, name='course_list'),

path('articles/', views.articles, name='article_list'),
path('events/', views.events, name='event_list'),
path('about/', views.about, name='about'),
path('faq/', views.faq, name='faq'),
path('contact/', views.contact, name='contact'),
path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
   path('dashboard/', views.dashboard, name='dashboard'),
]