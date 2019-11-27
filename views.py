import requests
import json
import os
from django.http import HttpResponse
from django.shortcuts import render, redirect

def replicator(request):
    context = {
        'active_link' : '/',
    }
    return render(request, 'the-replicator.html', context)


def about(request):
    context = {
        'active_link' : 'about/',
    }
    return render(request, 'about.html', context)


def meet_the_chef(request):
    context = {
        'active_link' : 'meet-the-chef/',
    }
    return render(request, 'meet-the-chef.html', context)

def contact(request):
    context = {
        'active_link' : 'contact/',
    }
    if request.POST:
        send_email(request)
    return render(request, 'contact.html', context)

# MailGun setup -------------------------
mailgun_api_key = os.environ["MAILGUN_API_KEY"]
# locate file or use heroku config to get API key then use the following bash command for each new terminal:
#     export MAILGUN_API_KEY="XXXXXXXXXXXXXXXXXXXXXX"

def mailgun(name, email, message):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxff6f95855b4243fea79d198ec524098d.mailgun.org/messages",
        auth=("api", mailgun_api_key),
        data={"from": (name, '<', email, '>'),
            "to": "Mish Mercer <mishell.mercer@gmail.com>",
            "subject": "Hello from " + name,
            "text": message})

def send_email(request):
    name = request.POST["name"]
    email = request.POST["email"]
    message = request.POST["message"]
    mailgun(name, email, message)
    redirect('/')