from django import forms
from .models import CustomUser


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')
