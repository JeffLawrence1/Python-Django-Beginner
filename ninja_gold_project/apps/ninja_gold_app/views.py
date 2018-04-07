# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from datetime import datetime
from random import randint

time = datetime.now().strftime("%H:%M %p, %B %d, %Y")
# Create your views here.
def index(request):   
    try:
        request.session['gold']
    except KeyError:
        request.session['gold'] = 0
    try:
        request.session['log']
    except KeyError:
        request.session['log'] = []
    return render(request, "ninja_gold_app/index.html")

def process_money(request):
    if request.POST['building'] == 'farm':
        rando1 = randint(1, 20)
        request.session['gold'] += rando1
        request.session['log'].append("You went to the farm and found {} gold!  {}".format(rando1, time))
    if request.POST['building'] == 'cave':
        rando2 = randint(1, 30)
        request.session['gold'] += rando2
        request.session['log'].append("You went in the cave and found {} gold!  {}".format(rando2, time))   
    if request.POST['building'] == 'house':
        rando3 = randint(1, 15)
        request.session['gold'] += rando3
        request.session['log'].append("You went in the house and found {} gold!  {}".format(rando3, time))
    if request.POST['building'] == 'casino':
        rando = randint(-100, 75)
        request.session['gold'] += rando
        if rando > 0:
            request.session['log'].append("You went to the casino and won {} gold!!!  {}".format(rando, time))
        elif rando == 0:
            request.session['log'].append("You went to the casino and broke even, at least you didn't lose! {}".format(time))
        elif rando < 0:
            request.session['log'].append("You went in the casino and lost {} gold!! You suck loser!!  {}".format(rando, time))
    return redirect('/')

def clear(request):
    request.session.flush()
    return redirect('/')