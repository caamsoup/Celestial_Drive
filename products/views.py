from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


# Create your views here.
def about(request):
    return render(request, "products/about.html")

def contact(request):
    return render(request, "products/contact.html")

def signin(request):
    return render(request, "products/signin.html")