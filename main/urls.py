from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('academics/', views.academics, name='academics'),
    path('admissions/', views.admissions, name='admissions'),
    path('contact/', views.contact, name='contact'),

    # ✅ Admission Form Save Route
    path('admission-form/', views.admission_view, name='admission_form'),

    # ✅ Success Page
    path('success/', views.success_view, name='success'),

    path("thank-you/", views.thank_you, name="thank_you"),
]