from django.shortcuts import render
from .models import Event


def home(request):
    context = {"events": Event.objects.all()}
    return render(request, "MainApp/home.html", context)


def events(request):
    return render(request, "MainApp/events.html", {})
