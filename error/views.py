from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('sorry you have encountered an error')