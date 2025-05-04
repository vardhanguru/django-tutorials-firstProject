from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def home_view(request):
    print("here")
    return HttpResponse("<h1>Hellow World</h1>")

def second_view(request):
    name = "Vardhan"
    return HttpResponse(f"<h1>My name is {str(name)}")

def time_view(request):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    return HttpResponse(f"<h2> current time is {time}</h2>")