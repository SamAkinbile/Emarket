from django.contrib import admin
from django.urls import path
from . import views
from homepage.views import custom_404


urlpatterns = [
    path('', views.index, name='homepage')
]

handler404 = 'homepage.views.custom_404'