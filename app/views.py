from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

# Create your views here.


def home(request):
    return render(request, "index.html")


def beliefs(request):
    return render(request, "beliefs.html")

def im_new(request):
    return render(request, "im_new.html")


def ministries(request):
    return render(request, "ministries.html")


def online_giving(request):
    return render(request, "online_giving.html")


def staff(request):
    return render(request, "staff.html")
