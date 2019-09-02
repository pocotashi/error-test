from django.http import HttpResponse
from django.shortcuts import render


productname = 'Yu-gi-oh cards'
yugioh_cards = ('Dark Magician', 'Blue Eyes White Dragon', 'Man eater bug', 'Kuriboh', 'Blue Eyes Toon Dragon')
Index = ('0', '1', '2', '3', '4')

def index(request):
    return HttpResponse('Yu-Gi-Oh cards')


def error(request):
    return HttpResponse(productname + " is sold out")


def new(request):
    return HttpResponse("New " + productname + " has arrived")


def getcard(request):
    return HttpResponse(yugioh_cards)


def productIndex(request, index = 0):
    if index >= len(yugioh_cards):
        return HttpResponse("card not found")
    else:
        message = str(yugioh_cards[index])
        return HttpResponse(message)

