from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from .models import Info

def home(request):
    return render(request, "lanapp/home.html")

def info(request, slug):
    info = get_object_or_404(Info, slug=slug)
    context = {
        "info": info
    }
    return render(request, "lanapp/index.html", context)
