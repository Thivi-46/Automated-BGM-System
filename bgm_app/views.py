from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import VideoForm

def home(request):
    return render(request, "bgm_app/home.html")

@login_required
def dashboard(request):
    return render(request, "bgm_app/dashboard.html")

def login(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            auth_login(request, user)

            messages.success(request, "Login Successful!")

            return redirect("dashboard")

        else:

            messages.error(request, "Invalid Username or Password.")

            return redirect("login")

    return render(request, "bgm_app/login.html")

def register(request):

    if request.method == "POST":
        print(request.POST)
        print("Username =", request.POST.get("username"))

        full_name = request.POST["full_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        # Password Check
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        # Username Exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        # Email Exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("register")

        # Create User
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=full_name
        )

        user.save()

        messages.success(request, "Registration Successful!")

        return redirect("login")

    return render(request, "bgm_app/register.html")

def logout(request):

    auth_logout(request)

    messages.success(request, "Logged out successfully.")

    return redirect("login")

@login_required
def upload(request):

    if request.method == "POST":

        form = VideoForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            messages.success(request, "Video uploaded successfully!")

            return redirect("dashboard")

    else:

        form = VideoForm()

    return render(
        request,
        "bgm_app/upload.html",
        {"form": form}
    )