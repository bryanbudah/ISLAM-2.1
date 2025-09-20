from django.shortcuts import render, redirect
from content.models import QuranQuote, Course, Article, Event
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import logout
from django.utils import timezone
from content.models import Article
from django.contrib.auth.decorators import login_required

# Home Page
def home(request):
    # 1. Get a random Quran quote
    quran_quote = QuranQuote.objects.order_by('?').first()

    # 2. Get 3 featured courses
    featured_courses = Course.objects.filter(
        is_featured=True
    ).order_by('-created_at')[:3]

    # 3. Get the latest article
    latest_article = Article.objects.filter(
        is_published=True
    ).order_by('-publish_date').first()

    # 4. Get the next upcoming event
    upcoming_event = Event.objects.filter(
        event_date__gte=timezone.now()
    ).order_by('event_date').first()

    context = {
        "quran_quote": quran_quote,
        "featured_courses": featured_courses,
        "latest_article": latest_article,
        "upcoming_event": upcoming_event,
        "show_hero": not request.user.is_authenticated,  # Show hero only when logged out
    }

    return render(request, "core/home.html", context)


# About Page
def about(request):
    return render(request, "content/about.html")


# Courses Page (use content app templates for consistency)
def courses(request):
    return render(request, "content/course_list.html")


# Articles Page
def articles(request):
    articles = Article.objects.filter(published=True).order_by('-created_at')
    return render(request, "content/article_list.html")


# Events Page
def events(request):
    return render(request, "content/event_list.html", {"events": Event.objects.all()})


# FAQ Page
def faq(request):
    return render(request, "content/faq.html")


# Contact Page
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Send email (optional)
        subject = f"New Contact Form Submission from {name}"
        body = f"Message:\n{message}\n\nFrom: {name} <{email}>"
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, ["your_email@example.com"])

        return render(request, "content/contact.html", {"success": True})

    return render(request, "content/contact.html")







