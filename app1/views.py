from django.shortcuts import render
from django.http import HttpResponse

def tarun(request):
    return HttpResponse('this is string1 of app1')

def varsha(request):
    return HttpResponse('<h1><marquee> congratulations</marquee></h1>')

# Create your views here.
