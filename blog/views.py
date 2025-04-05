from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from .forms import ContactForm
from .models import NewsletterSubscription
from .forms import NewsletterForm
from .forms import EvaluationForm



def newsletter_subscription(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Subscribed to newsletter successfully!")
            return redirect('blog_home')  # Change to your desired redirect URL
    else:
        form = NewsletterForm()
    return render(request, 'blog/newsletter_form.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('blog_home')  # Change to your desired redirect URL
    else:
        form = ContactForm()
    return render(request, 'blog/contact_form.html', {'form': form})

def evaluation(request):
    if request.method == 'POST':
        form = EvaluationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your evaluation has been submitted successfully!")
            return redirect('blog_home')  # Redirect after submission
    else:
        form = EvaluationForm()
    return render(request, 'blog/evaluation.html', {'form': form})




def blog_home(request):
    return render(request, 'blog/blog.html')
