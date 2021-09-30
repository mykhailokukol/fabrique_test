from django import forms
from . import models


class LoginForm(forms.Form):

    username = forms.CharField(max_length=255, required=True, label='Никнейм')
    password = forms.CharField(widget=forms.PasswordInput(), required=True, label='Пароль')


class CreateQuizForm(forms.ModelForm):

    class Meta:

        model = models.Quiz
        fields = ['title', 'date_finish', 'description']
        widgets = {
            'date_finish': forms.SelectDateWidget(),
            'description': forms.Textarea(),
        }


class CreateQuestionForm(forms.ModelForm):

    class Meta:

        model = models.Question
        fields = ['text', 'type']
        widgets = {
            'type': forms.RadioSelect(),
        }
