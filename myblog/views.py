from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


# Create your views here
@login_required(login_url='login')
def index(request):
    return render(request, 'myblog/index.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, 'myblog/thanks.html')
        else:
            form = ContactForm()
            context = {'form': form, 'error_message': 'The data entered is not valid!'}
            return render(request, 'myblog/contact.html', context)
    else:
        form = ContactForm()
        context = {'form': form}
        return render(request, 'myblog/contact.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'myblog/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'myblog/register.html', context)

