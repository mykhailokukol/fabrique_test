from django import forms
from . import models


class LoginForm(forms.Form):

    username = forms.CharField(max_length=255, required=True, label='Никнейм')
    password = forms.CharField(widget=forms.PasswordInput(), required=True, label='Пароль')
