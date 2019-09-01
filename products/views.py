from django.http import HttpResponse
from django.shortcuts import render


productname = 'Yu-gi-oh cards'
def index(request):
    return HttpResponse('hello world')
def error(request):
    return HttpResponse('there is an error with' + productname)