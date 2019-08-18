from django import forms
from django.contrib.auth.models import User


class Login(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput())
    password = forms.CharField(label='', widget=forms.PasswordInput())


class SignIn(forms.ModelForm):
    re_password = forms.CharField(label='', widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['username', 'password', 'email', 'first_name', 'last_name']:
            self.fields[field_name].help_text = None
            self.fields[field_name].label = ''

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    def is_valid(self):
        return super().is_valid() and self.cleaned_data['re_password'] == self.cleaned_data['password']
