from django.shortcuts import render, redirect
from .models import Admission
from django.core.mail import send_mail
from django.conf import settings
from .forms import AdmissionForm
from django.contrib import messages
from .models import ContactMessage

from django.contrib.auth.models import User
from django.http import HttpResponse

def home(request):
    total_admissions = Admission.objects.count()
    return render(request, 'index.html', {
        'total_admissions': total_admissions
    })

def about(request):
    return render(request, 'about.html')


def academics(request):
    return render(request, 'academics.html')


def contact(request):
    return render(request, 'contact.html')


def admissions(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        grade = request.POST.get("grade")
        message = request.POST.get("message")

        # 1️⃣ Save to database
        Admission.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            grade=grade,
            message=message
        )

        # 2️⃣ Send email notification
#         send_mail(
#             subject="New Admission Form Submitted",
#             message=f"""
# New Admission Details:

# Name: {full_name}
# Email: {email}
# Phone: {phone}
# Grade: {grade}
# Message: {message}
# """,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[settings.EMAIL_HOST_USER],
#             #fail_silently=False,
#             fail_silently=True
#         )

        return redirect("thank_you")

    return render(request, "admissions.html")


def thank_you(request):
    return render(request, "thank_you.html")


def admission_view(request):
    if request.method == "POST":
        form = AdmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = AdmissionForm()
    
    return render(request, 'admission.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message_text = request.POST.get("message")

        # Save to Database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message_text
        )

        # Send Email
        send_mail(
            subject=f"New Contact Message: {subject}",
            message=f"""
New Contact Message:

Name: {name}
Email: {email}
Subject: {subject}
Message: {message_text}
""",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        messages.success(request, "Message sent successfully!")

        return redirect("contact")

    return render(request, "contact.html")


def create_admin(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@gmail.com", "admin123")
        return HttpResponse("Admin created")
    return HttpResponse("Admin already exists")