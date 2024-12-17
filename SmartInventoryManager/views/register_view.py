from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest

User = get_user_model()

def register(request: HttpRequest):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone_number = request.POST.get("phone_number")
        address = request.POST.get("address")

        if not (first_name and last_name and email and password and phone_number and address):
            return render(request, "register.html", {"error": "All fields are required."})

        if User.objects.filter(email=email).exists():
            return render(request, "register.html", {"error": "A user with this email already exists."})

        User.objects.create(
            username=email,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=make_password(password),
            phone_number=phone_number,
            address=address,
            role="customer"
        )
        return redirect("home")

    return render(request, "register.html")