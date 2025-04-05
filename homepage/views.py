from django.shortcuts import render
from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'homepage/index.html')

def custom_404(request, exception):

    return render(request, "homepage/404.html")