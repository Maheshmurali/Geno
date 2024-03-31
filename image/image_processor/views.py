
from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image #database puthiya data base add cheyyan modelil poyi add akki ivedae import cheyyanam



def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES) #upload cheyyunna image edukkan
        if form.is_valid(): #image undangil matharam next page varu
            form.save() #varunna image data baseil save cheyyan
            ''' ivedae ninakk venda code ezhthanam
            
            
             '''
            return redirect('result') #result page load cheyyan
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form}) # form htmlil load cheyyan

def result(request):
    last_image = Image.objects.latest('uploaded_at') # last image db nn edukkan ulla queary
    ''' njan ith last image akki ann set cheyithirikkunnath ath matti ith matti venda image load cheyyam'''

    return render(request, 'result.html', {'last_image': last_image}) #last image html pagelil load cheyyan
    

