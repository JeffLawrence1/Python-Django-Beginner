# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):  
    context = {
        "items": items
    }  
    return render(request, "amadon_app/index.html", context)

def checkout(request):
    return render(request, "amadon_app/checkout.html")

def clear(request):
    request.session.flush()
    return redirect('/')

items = [
    {
        "id": 1,
        "name": "Dojo T-Shirt",
        "price": 19.99,
    },
    {
        "id": 2,
        "name": "Dojo Sweater",
        "price": 29.99
    },
    {
        "id": 3,
        "name": "Dojo Cup",
        "price": 4.99
    },
    {
        "id": 4,
        "name": "Algorithm Book",
        "price": 49.99
    },
        {
        "id": 5,
        "name": "Dojo T-Shirtsdfd",
        "price": 19.99,
    },
    {
        "id": 6,
        "name": "Dojo Sweatersdfsdfsd",
        "price": 29.99
    },
    {
        "id": 7,
        "name": "Dojo Cupsdfsdf",
        "price": 4.99
    },
    {
        "id": 8,
        "name": "Algorithm Booksdfsdfds",
        "price": 49.99
    },
]

def buy(request, pid):
    for item in items:
        if item['id'] == int(pid):
            cost = item['price'] * int(request.POST['amount'])

    try:
        request.session['total']
    except KeyError:
        request.session['total'] = 0
    try:
        request.session['item']
    except KeyError:
        request.session['item'] = 0

    request.session['total'] += cost
    request.session['item'] += int(request.POST['amount'])
    request.session['checkout'] = cost
    return redirect('/checkout')
    

