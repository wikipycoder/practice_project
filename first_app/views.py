from django.shortcuts import render
from django.http import HttpResponse

def index(request): 
    return HttpResponse("hello world")

def login(request):
    return HttpResponse("this is a login page")