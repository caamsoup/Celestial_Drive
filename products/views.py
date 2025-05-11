from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm


# Create your views here.
def about(request):
    return render(request, "products/about.html")

def contact(request):
    return render(request, "products/contact.html")

def signin(request):
    return render(request, "products/signin.html")

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/thank_you.html')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
