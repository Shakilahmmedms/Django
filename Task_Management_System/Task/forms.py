from django import forms
from  Task.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'task_date' : forms.DateInput(attrs={'type':'date'})
        }