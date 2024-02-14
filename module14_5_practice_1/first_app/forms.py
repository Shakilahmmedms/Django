from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label='User Name', help_text='Enter Atleast 10 characters')
    age = forms.IntegerField(label='Age')
    email = forms.EmailField(label='Email')
    check = forms.BooleanField()
    birthday = forms.CharField(widget= forms.DateInput(attrs={'type': 'date'}))
    appointment = forms.CharField(widget= forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    CHOISE = [('S','Small'), ('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices=CHOISE)
    commments = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    COLORS = [('B','Blue'),('G','Green'),('BL','Black')]
    color = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=COLORS)
    