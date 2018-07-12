from django.shortcuts import render, redirect
# Create your views here.
def index(request):
    if 'words' not in request.session:
        request.session['words']={}
    return render(request,'session_words_app/index.html')

def process(request, methods=['POST']):
    request.session['word'] = request.POST['newword']
    request.session['color'] = request.POST['radio']
    request.session['size'] = request.POST['bigfont']
    print("WORD: ",request.session['word'])
    print("COLOR: ",request.session['color'])
    print("BIG: ",request.session['size'])
    temp_list = [request.session['words']]
    temp_list.append({"word": request.session['word'], "color": request.session['color'], "show_big": request.session['size']})
    request.session['words'] = temp_list
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')