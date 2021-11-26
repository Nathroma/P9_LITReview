from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """
    Créer un nouvel utilisateur
    """
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('login')
        else:
            form = UserCreationForm()
        return render(request, 'register.html', {'form': form})


def disconnect(request):
    """
    Déconnecte l'utilisateur actuel
    """
    logout(request)
    return redirect('login')
