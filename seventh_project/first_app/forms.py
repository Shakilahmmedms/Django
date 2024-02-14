from django import forms
from .import models

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.StudentModel
        # exclude = ['roll']
        fields = '__all__'
        labels ={
            'name': 'Student Name',
             'roll': 'Student Roll'
        }
        widgets = {
            'name' : forms.TextInput(),
            # 'roll' : forms.PasswordInput()
        }

        help_texts ={
            'name': 'Enter Your Full Name'
        }
        error_messages = {
            'roll' :{'required':'Your Roll is Required'},
        }