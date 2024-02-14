from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    dit = {'author':'Ami', 'age':21,'lst':['Python','is','best'],'birthDay':datetime.datetime.now(),'val':'' ,'courses': [
        {
            'id':1,
            'name': 'Python',
            'fee':5000
        },
        {
            'id':2,
            'name': 'Django',
            'fee':4000
        },
        {
            'id':3,
            'name': 'C Program',
            'fee':1000
        },
    ]}
    return render(request, 'home.html',dit)
