from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login

from . import forms


def login_page(request):
    form = forms.Login()
    if request.method == 'POST':
        form = forms.Login(request.POST)
        if form.is_valid():
            user_login(request, form)

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('username', kwargs={
            'username': request.user.username
        }))

    return render(request, 'main/login.html', {
        'form': form,
    })


def user_login(request, form):
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)


def sign_in_page(request):
    form = forms.SignIn()
    if request.method == 'POST':
        form = forms.SignIn(request.POST)
        if form.is_valid():
            form.save()
            user_login(request, form)

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('username', kwargs={
            'username': request.user.username
        }))

    return render(request, 'main/sign_in.html', {
        'form': form,
    })
