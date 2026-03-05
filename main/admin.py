
# Register your models here.
from django.contrib import admin
from .models import Admission
from .models import ContactMessage

admin.site.register(ContactMessage)

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "grade", "created_at")
    search_fields = ("full_name", "email", "phone")
    list_filter = ("grade", "created_at")
    ordering = ("-created_at",)

