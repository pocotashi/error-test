from django.http import HttpResponse
from django.shortcuts import render


productname = 'Yu-gi-oh cards'
yugioh_cards = ('dark magician', 'blue eyes WD', 'man eater bug', 'kuriboh', 'toon BEWD')


def index(request):
    return HttpResponse('hello world')


def error(request):
    return HttpResponse(productname + " is sold out")


def new(request):
    return HttpResponse("New " + productname + " has arrived")

def getcard(request):
    return HttpResponse(yugioh_cards)

def getcard0(request):
    return HttpResponse(yugioh_cards[0])


def getcard1(request):
    return HttpResponse(yugioh_cards[1])


def getcard2(request):
    return HttpResponse(yugioh_cards[2])


def getcard3(request):
    return HttpResponse(yugioh_cards[3])


def getcard4(request):
    return HttpResponse(yugioh_cards[4])