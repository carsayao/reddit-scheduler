from socket import fromshare
from django import forms
from django.forms import ModelForm
from .models import Content

class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = ('default_title', 'kind')