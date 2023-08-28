from django import forms
from django.contrib.auth.models import User
from .models import Profile

#It's used  to edit user-related information
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name","last_name","email")

#It's used to edit the Profile model's information 
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("photo",)
        

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name')  
        
    def clean_password2(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError('Passwords do not match')
        return self.cleaned_data['password2']





