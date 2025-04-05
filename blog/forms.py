from django import forms
from .models import NewsletterSubscription
from .models import Contact
from .models import Evaluation



class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

from django import forms
from .models import Evaluation

class EvaluationForm(forms.ModelForm):
    comments = forms.CharField(widget=forms.Textarea())  # Use a plain Textarea for comments

    class Meta:
        model = Evaluation
        fields = '__all__'
