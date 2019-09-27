# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


# Create your views here.
def view1(request):
    return render(request, "home.html")


def login_view(request):
    return render(request, 'login.html')


def register_view(request):
    return render(request, 'register.html')


def view_404(request):
    return render(request, '404.html')


def fpass_view(request):
    return render(request, 'forgot-password.html')
