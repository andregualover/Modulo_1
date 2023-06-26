from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def sobre(request):
    return HttpResponse('sobre')

def home(request):
    return HttpResponse('home')