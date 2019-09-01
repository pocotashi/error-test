from django.http import HttpResponse
from django.shortcuts import render


productname = 'Yu-gi-oh cards'
def index(request):
    return HttpResponse('hello world')
def soldout(request):
    return HttpResponse(productname + " is sold out")
