from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Majburiy. To‘g‘ri email kiriting.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'class': 'w-full p-2 border rounded'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'image')
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'class': 'w-full p-2 border rounded'}),
        }

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'w-full p-2 border rounded'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'class': 'w-full p-2 border rounded'}))