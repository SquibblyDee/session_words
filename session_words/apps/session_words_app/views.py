from django.shortcuts import render, redirect
from datetime import datetime
# Create your views here.
# Initialize an empty session['words'] if it doesn't exist and go to index
def index(request):
    if 'words' not in request.session:
        request.session['words']=[]
    return render(request,'session_words_app/index.html')

# We can't append to a dict so we have to assign it to a temp variable, append new data to it, then reassign it to the session
def process(request, methods=['POST']):
    print(request.POST)
    format="%H:%M:%S %m %d %Y"
    request.session['datetime'] = datetime.strftime(datetime.now(),format)
    temp_list = request.session['words']
    temp_list.append({"word": request.POST['newword'], "color": request.POST['radio'], "show_big": request.POST['bigfont'], "datetime": request.session['datetime']})
    request.session['words'] = temp_list
    return redirect('/')

# Just clears out session
def clear(request):
    request.session.clear()
    return redirect('/')