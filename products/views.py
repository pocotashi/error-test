from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('hello world')
def error(request):
    return HttpResponse('there is an error with this product')