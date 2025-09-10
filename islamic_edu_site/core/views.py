from django.shortcuts import render
from content.models import QuranQuote, Course, Article, Event  # Import your models

def home_view(request):
    # 1. Get a random Quran quote
    quran_quote = QuranQuote.objects.order_by('?').first()  # Random quote
    
    # 2. Get 3 featured courses
    featured_courses = Course.objects.filter(
        is_featured=True
    ).order_by('-created_at')[:3]
    
    # 3. Get the latest article
    latest_article = Article.objects.filter(
        is_published=True
    ).order_by('-publish_date').first()
    
    # 4. Get the next upcoming event
    from django.utils import timezone
    upcoming_event = Event.objects.filter(
        event_date__gte= timezone.now()
    ).order_by('event_date').first()
    
    context = {
        'quran_quote': quran_quote,
        'featured_courses': featured_courses,
        'latest_article': latest_article,
        'upcoming_event': upcoming_event,
    }
    
    return render(request, 'core/home.html', context)

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')
def courses(request):
    return render(request, 'content/courses.html')
def articles(request):
    return render(request, 'content/articles.html')
def events(request):
    return render(request, 'events.html', {'events': Event.objects.all()})
# core/views.py
def course_list(request):
    return render(request, 'core/courses.html')
# In core/views.py
def courses(request):
    return render(request, 'core/courses.html')
def courses_view(request):
    return render(request, 'core/courses.html')
from django.shortcuts import render

def about(request):
    return render(request, 'core/about.html')

def faq(request):
    return render(request, "core/faq.html")