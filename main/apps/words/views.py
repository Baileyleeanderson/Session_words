from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime
import datetime

def index(request):
    if not "datetime" in request.session:
       request.session['words'] = []
    return render(request,'words/index.html',)

def process(request):
    word_dict = {
        'words' : request.POST['name'],
        'colors' : request.POST['color'],
        'date' : 'added on' + ' ' + str(datetime.datetime.now()) + '\n',
    }
    newlist = request.session['words']
    newlist.append(word_dict)
    request.session['words'] = newlist
    if 'checkbox' not in request.POST:
        word_dict['fontsize'] = 'small'
    else: 
        word_dict['fontsize'] = request.POST['checkbox']
    return redirect('/session_words/addword')

def add(request):
    return render(request,'words/index.html')

def clear(request):
    
    del request.session['words']
    return redirect('/')


