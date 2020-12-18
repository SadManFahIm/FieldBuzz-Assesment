from django import forms
from . models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model  = Person


class LoginForm(forms.Form):
    username = forms.CharField(label='Enter your Username')
    password = forms.PasswordInput()
