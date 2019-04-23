from django.shortcuts import render,redirect


def home(request):
    return render(request, 'base/home.html', {})


def not_found(request):
    return render(request, 'base/not_found.html', {})
