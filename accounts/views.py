from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('informations:index')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/form.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'informations:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/form.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('informations:index')