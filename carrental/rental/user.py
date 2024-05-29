from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages

def login(request):
     return render(request, 'login.html.jinja')

def logout(request):
    return render(request, 'logout.html.jinja')

def register(request):
    if request.method == 'POST':
        form_user = forms.RegistrationForm(request.POST)
        form_address = forms.UserAddressFormSet(request.POST)
        if form_user.is_valid() and form_address.is_valid():
            user = form_user.save()
            addresses = form_address.save(commit=False)
            for address in addresses:
                address.user = user
                addresses.save()
            return redirect(request, 'register.html.jinja', {'message' : "success"})
        return redirect(request, 'register.html.jinja', {'message' : "fail"})
    else:
        form_user = forms.RegistrationForm()
        form_address = forms.RegistrationForm()
        return render(request, 'register.html.jinja', {'form_user': form_user, 'form_address':form_address})