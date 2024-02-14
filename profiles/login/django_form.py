from django import forms

class DjangoLoginForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()