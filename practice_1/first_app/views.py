from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    d ={ 'name': 'Shakil','age':21,'date':datetime.datetime.now(),'lst':['Rahim','karim','Rafiq'], 'courses':[
        {
            'id':1,
            'name':'Python',
            'fee': 6500,
        },
        {
            'id':1,
            'name':'Django',
            'fee': 6500,
        },
        {
            'id':1,
            'name':'C plus',
            'fee': 6500,
        },
    ]}
    return render(request,'index.html',d)