from django.shortcuts import render

def home(request):
    return render(request, "bgm_app/home.html")

def login(request):
    return render(request, "bgm_app/login.html")