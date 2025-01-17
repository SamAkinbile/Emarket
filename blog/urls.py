from django.urls import path
from .views import contact
from . import views
from .views import newsletter_subscription


urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('contact/', contact, name='contact_form'),
    path('subscribe/', newsletter_subscription, name='newsletter_subscription'),
]
