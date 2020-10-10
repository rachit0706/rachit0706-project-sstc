from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,User
from .models import StudentProfile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
  

    class Meta:
        model = User
        fields = ['username','email']
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProfileUpdateForm(forms.ModelForm):

    
    class Meta:
        model = StudentProfile
        fields = ['image']

        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'})
            }


