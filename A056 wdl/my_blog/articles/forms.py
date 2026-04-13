from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'input-field w-full px-4 py-3 rounded-xl text-white placeholder-white placeholder-opacity-60 focus:outline-none',
                'placeholder': 'Enter a title for your article',
            }),
            'content': forms.Textarea(attrs={
                'class': 'input-field w-full px-4 py-3 rounded-xl text-white placeholder-white placeholder-opacity-60 focus:outline-none h-48',
                'placeholder': 'Share your story...',
            }),
        }
        labels = {
            'title': 'Title',
            'content': 'Content',
        }
