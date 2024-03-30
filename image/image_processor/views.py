
from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image



def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('result')
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})

def result(request):
    last_image = Image.objects.latest('uploaded_at')
    return render(request, 'result.html', {'last_image': last_image})
    

