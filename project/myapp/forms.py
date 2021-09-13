from django import forms
from django.forms import fields

from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('book_name', 'author', 'rating')
        
