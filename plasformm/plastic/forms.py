from django import forms
from .models import ContactModel
from django.forms import ModelForm

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'company', 'email', 'number', 'description']
