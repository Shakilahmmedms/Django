from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label='User Name')
    age = forms.IntegerField(label='Age')
    email = forms.EmailField(label='Email')