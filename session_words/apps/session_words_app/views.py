from django.shortcuts import render, redirect
# Create your views here.
def index(request):
    return render(request,'session_words_app/index.html')

def process(request, methods=['POST']):
    request.session['word'] = request.POST['newword']
    request.session['color'] = request.POST['radio']
    request.session['size'] = request.POST['bigfont']
    print("WORD: ",request.session['word'])
    print("COLOR: ",request.session['color'])
    print("BIG: ",request.session['size'])

    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')