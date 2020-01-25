from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())
    school = forms.CharField(max_length=200)
