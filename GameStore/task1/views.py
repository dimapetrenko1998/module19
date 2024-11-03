from django.shortcuts import render, redirect
from .models import Game, Buyer
from .forms import RegistrationForm

# Create your views here.


# Главная страница
def home(request):
    return render(request, 'task1/home.html')


# Список товаров
def product_list(request):
    games = Game.objects.all()
    return render(request, 'task1/product_list.html', {'games': games})


# Корзина
def cart(request):
    return render(request, 'task1/cart.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Храните пароль в зашифрованном виде
            user.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'task1/register.html', {'form': form})
