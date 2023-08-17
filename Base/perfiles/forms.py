from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name','username']
		

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image','bio']