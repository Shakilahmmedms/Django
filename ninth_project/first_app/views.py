from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse
# Create your views here.
def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name','sinthi', expires=datetime.utcnow()+timedelta(days=7))
    return response

def get_cookies(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, 'get_cookie.html', {'name':name})

def delete_cookie(request):
    response = render(request,'del.html')
    response.delete_cookie('name')
    return response


# session vs cookies
def set_session(request):
    # data = {
    #     'name': 'rahim',
    #     'age':23,
    #     'language': 'Bangla',
    # }
    # request.session.update(data)
    request.session['name'] = 'karim'
    return render(request, 'home.html')

def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name','Guest')
        # age = request.session.get('age')
        request.session.modified = True
        return render(request, 'get_session.html',{'name' : name})
    else:
        return HttpResponse('Your Session has been expired , Login again')

def delet_session(request):
    # del request.session['name']
    request.session.flush()
    return render(request,'del.html')