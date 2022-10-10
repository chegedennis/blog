from .models import Comment
from django import forms
from django.forms import Textarea, EmailInput, TextInput

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'email', 'body')
        labels = {
            'author': ('Name'),
            'body': ('Comment'),
        }

        widgets = {
            'author': TextInput(attrs={
                # 'class': 'form-control',
                'style': 'width:90%;',
                'placeholder': 'Name'
            }),
            'email': EmailInput(attrs={
                # 'class': 'form-control',
                'style': 'width:90%',
                'placeholder': 'Email'
            }),
            'body': Textarea(attrs={
                'rows':3,
                'class': 'form-control', 
                'style':'width:90%',
                'placeholder':'Enter your comment'
            })
        }

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width:90%;',
                'placeholder': 'Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                'class': 'form-control',
                'style': 'width:90%',
                'placeholder': 'Email'
            }))
    message = forms.CharField(widget=forms.Textarea(attrs={
                'rows':3,
                'class': 'form-control', 
                'style':'width:90%',
                'placeholder':'Enter your Message'
            }))