from django.shortcuts import render
from django.http import HttpResponse
import json

path = '/home/eitan/Desktop/planck/mysite/tenbismenu/data.json'
f = open(path)
data = json.load(f)

z=2

def index(request):
    # print(str(request))
    # data = sendData()

    return HttpResponse('')
# Create your views here.


def drinks(request):
    str = 'drinks'
    return HttpResponse(sendData(str))

def specDrink(request, id):
    str = "specDrink"
    return HttpResponse(sendData2(str, id))


def pizza(request):
    str = 'pizzas'
    return HttpResponse(sendData(str))


def specPizza(request, id):
    str = "specPizza"
    return HttpResponse(sendData2(str, id))


def desserts(request):
    str = 'desserts'
    return HttpResponse(sendData(str))



def specDessert(request, id):
    str = "specDessert"
    return HttpResponse(sendData2(str, id))


def sendData(strToSend):
    categoryNum = 0
    if strToSend == 'drinks':
        categoryNum = 5
    elif strToSend == 'pizzas':
        categoryNum = 3
    elif strToSend == 'desserts':
        categoryNum = 4
    itemsList = ""
    for item in data['Data']['categoriesList'][categoryNum]['dishList']:
        id = item['dishId']
        name = item['dishName']
        description = item['dishDescription']
        price = item['dishPrice']
        itemsList = itemsList +  'the id is: ' + str(id) + ', the name is: ' + name + ', the description is: ' + description + ', the price is: ' + str(price) + '. \n'
    return itemsList

def sendData2(strToSend, item_id):
    categoryNum = 0
    if strToSend == 'drinks':
        categoryNum = 5
    elif strToSend == 'pizzas':
        categoryNum = 3
    elif strToSend == 'desserts':
        categoryNum = 4
    itemsList = ""
    for item in data['Data']['categoriesList'][categoryNum]['dishList']:
        if str(item_id) == str(item['dishId']):
            id = item['dishId']
            name = item['dishName']
            description = item['dishDescription']
            price = item['dishPrice']
            itemsList = 'the id is: ' + str(id) + ', the name is: ' + name + ', the description is: ' + description + ', the price is: ' + str(price) + '. \n'
    return itemsList
    
    
    tosend = strToSend +' '+ str(id)
    return tosend
