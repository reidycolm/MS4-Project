from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    # Post Form
    class Meta:
        model = Post
        fields = ['title', 'author' ,'content', 'status']