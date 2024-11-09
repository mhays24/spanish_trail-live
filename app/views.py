from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpRequest
from django.core.mail import send_mail
from django.conf import settings

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

def send_question(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        # Construct the email message
        full_message = f"Name: {name}\nEmil: {email}\n\nMessage:\n{message}"
        
        # Send email
        send_mail(
            subject=f" Question from Question from {name}",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
        
        return redirect("home")
    return render(request, "im_new.html")
