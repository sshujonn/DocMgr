from django import forms





class SignUpForm(forms.Form):
    fullname = forms.CharField()
    username = forms.CharField()
    password = forms.CharField()
    confirm_password = forms.CharField()
    email = forms.CharField()