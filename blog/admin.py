from django.contrib import admin
from .models import Evaluation


# Register your models here.

from django.contrib import admin
from .models import NewsletterSubscription, Contact

@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')  # Fields to display in the list view
    search_fields = ('email',)  # Enable search by email
    list_filter = ('subscribed_at',)  # Enable filtering by subscription date

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at')  # Fields to display in the list view
    search_fields = ('name', 'email', 'subject')  # Enable search by name, email, or subject
    list_filter = ('submitted_at',)  # Enable filtering by submission date

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "rating", "submitted_at")
    search_fields = ("name", "email", "rating")
