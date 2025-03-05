from django.shortcuts import render, redirect
from .forms import BorderForm
from .models import Borders

# Home View
def home(request):
    form = BorderForm()
    
    if request.method == 'POST':
        form = BorderForm(request.POST)
        if form.is_valid():  
            form.save()
            return redirect('home')  
    
    data = Borders.objects.all()

    context = {
        'form': form,
        'data': data,
    }
    return render(request, 'index.html', context)


# Delete View
def Delete_records(request, id):
    a = Borders.objects.get(pk=id)  
    a.delete()
    return redirect('home') 


# Update View
def Update_records(request, id):
    data = Borders.objects.get(pk=id)

    if request.method == 'POST':
        form = BorderForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('home')  

    else:
        form = BorderForm(instance=data)

    context = {
        'form': form,
    }
    return render(request, 'update.html', context)
