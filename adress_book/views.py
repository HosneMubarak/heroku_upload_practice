from django.shortcuts import render, redirect
from .models import Address
from .forms import AddressForm
from django.contrib import messages


# Create your views here.

def home(request):
    all_address = Address.objects.all()
    return render(request, 'home.html', {'all_address': all_address})


def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Address adder!'))
            return redirect('home')
        else:
            messages.success(request, ('Seems some thisng worng!!!!'))
            return redirect('add-address')
    else:
        return render(request, 'add_address.html', {})


def editView(request, list_id):
    if request.method == 'POST':
        current_address = Address.objects.get(pk=list_id)
        form = AddressForm(request.POST or None, instance=current_address)
        if form.is_valid():
            form.save()
            messages.success(request, ("adress updated!!!"))
            return redirect('home')
        else:
            messages.success(request, ("Cant Update!"))
            return render(request, 'edit.html')
    else:
        get_address = Address.objects.get(pk=list_id)
        return render(request, 'edit.html', {'get_address': get_address})


def deleteView(request, list_id):
    if request.method == 'POST':
        current_address = Address.objects.get(pk=list_id)
        current_address.delete()
        messages.success(request, ("adress deleted!!"))
        return redirect('home')
