from django.shortcuts import render, redirect
from .models import Buyer, Game
from .forms import RegistrationForm
from .models import Buyer


def home(request):
    return render(request, 'object_detection/home.html')


def products(request):
    games = Game.objects.all()
    return render(request, 'object_detection/products.html', {'games': games})


def cart(request):
    return render(request, 'object_detection/cart.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if not Buyer.objects.filter(name=username).exists():
                Buyer.objects.create(name=username, balance=0.00, age=18)
                return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'object_detection/registration.html', {'form': form})


