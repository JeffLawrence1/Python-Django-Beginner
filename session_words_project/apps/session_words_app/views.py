# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, redirect

# datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Create your views here.
def index(request):
    return render(request, "session_words_app/index.html")

def clear(request):
    request.session.clear()
    return redirect('/')

def add(request):
    word = {}
    for key, value in request.POST.items():
        if key != 'csrfmiddlewaretoken' and key != 'show_big':
            word[key] = value
        if key == 'show_big':
            word['big'] = "big"
        else:
            word['big'] = ""
    word['creation'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        request.session['word']
    except KeyError:
        request.session['word'] = []

    temp = request.session['word']
    temp.append(word)
    request.session['word'] = temp
    # for key, val in request.session.__dict__.iteritems():
    #     print key, val
    # print "created", word

    return redirect('/')