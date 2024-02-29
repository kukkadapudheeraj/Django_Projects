from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def calculate(request):
    return HttpResponse(2+3)

def say_hello(request):
    # return HttpResponse('Hello World')
    return render(request, 'hello.html', {"name": "Dheeraj"})
