from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, PasswordInput

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    widgets = {
        'username': TextInput(attrs={
                'id': 'exampleInputEmail1',
                'aria-describedby': 'emailHelp',
                'class': 'form-control',
                'placeholder': 'Enter email'
            }),
        'password': PasswordInput(attrs={
                'id': 'exampleInputPassword1',
                'type': 'password',
                'class': 'form-control',
                'placeholder': 'Пароль'
            }),
    }