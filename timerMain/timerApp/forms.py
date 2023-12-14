from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, EmailValidator

class RegisterForm(UserCreationForm):
    username = forms.CharField(validators=[MinLengthValidator(5)], error_messages={'required': 'Please enter a username.'})
    email = forms.EmailField(validators=[EmailValidator()], error_messages={'required': 'Please enter an email address.'})
    password1 = forms.CharField(validators=[MinLengthValidator(8)], error_messages={'required': 'Please enter a password.'})
    password2 = forms.CharField(validators=[MinLengthValidator(8)], error_messages={'required': 'Please confirm your password.'})

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already in use.")
        return email