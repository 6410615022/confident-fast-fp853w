from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #return HttpResponse('<h1>Hello, World!</h1>')
    return render(request, 'hello/index.html')

def greet(request, name):
    from django.utils import timezone
    #return HttpResponse(f'<h1>Hello, {name}!</h1>')
    return render(request, 'hello/greet.html', {
        'name': name.title(),
        'hour': hour
        },)
    