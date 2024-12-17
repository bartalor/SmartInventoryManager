from django.http import HttpRequest
from django.shortcuts import render
import typeguard

@typeguard.typechecked
def home(request: HttpRequest):
    return render(request, "home.html", {"user": request.user})
