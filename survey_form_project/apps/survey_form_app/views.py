# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request): 
    return render(request, "survey_form_app/index.html")

def results(request):
    return render(request, "survey_form_app/landing.html")

def info(request):
    try:
        request.session['tries']
    except KeyError:
        request.session['tries'] = 0
    
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    request.session['tries'] += 1

    return redirect('/results')