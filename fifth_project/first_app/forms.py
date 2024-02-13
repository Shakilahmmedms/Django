from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(label='User Name', help_text='Enter Your Full Name within 10 characters')

    # file = forms.FileField()

    email = forms.EmailField(label='Emagil Address')
    age = forms.IntegerField(label='Age')
    weigth = forms.FloatField(label='Weight')
    balance = forms.DecimalField()
    Check = forms.BooleanField()
    birthday = forms.CharField(widget=forms.DateInput(attrs={'type': 'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))
    CHOICES = [('S','Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    MEAL = [('P','Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizz = forms.MultipleChoiceField(choices= MEAL, widget= forms.CheckboxSelectMultiple)

# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
#     age = forms.CharField()
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError('Enter Atleast 10 characters')
    #     return valname
    
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('Your email must contain .com')
    #     return valemail

    # def clean(self):
    #     clean_data = super().clean()
    #     valname = clean_data['name']
    #     valemail = clean_data['email']
    #     if len(valname) <10:
    #         raise forms.ValidationError('Enter Mus be 10 characters')
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('You email contains must be .com')

def len_check(value):
    if len(value) <10:
        raise forms.ValidationError('Enter must be 10 characters')


class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput , validators=[validators.MinLengthValidator(10, message='Enter Must be 10 characters')])
    text = forms.CharField(validators=[len_check])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message='Enter a valid Email')])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(34, message='Age must be 18 to 34'), validators.MinValueValidator(18 , message='Age must be 18 to 34')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'])])


class passworValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        con_pass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']

        if val_pass != con_pass:
            raise forms.ValidationError('Password did not match')
        if len(val_name) < 10:
            raise forms.ValidationError('Enter atleast 10 characters')