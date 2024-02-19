from django import forms
from .models import CarPosts,Comment

class CarForm(forms.ModelForm):
    class Meta:
        model = CarPosts
        fields = '__all__'
        # exclude = ['author']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']
        # exclude = ['author']