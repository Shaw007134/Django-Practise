from django import forms

from .models import BlogPost

class NewBlogForm(forms.ModelForm):
    """发布新博客表单"""
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': '', 'text': ''}

class EditBlogForm(forms.ModelForm):
    """编辑现有博客表单"""
    class Meta:
        model = BlogPost
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 100})}


        
