import requests
import json
from django.http import HttpResponse
from django.shortcuts import render

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
    return render(request, 'contact.html', context)

# MailGun example email method -----------------------------------------------------------------
def send_message(name, email, message):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxff6f95855b4243fea79d198ec524098d.mailgun.org/messages",
        auth=("api", "010b9271dac02ac74fec58f880dca8c5-09001d55-e01ed707"),
        data={"from": (name, email),
            "to": "Mish Mercer <mishell.mercer@gmail.com>",
            "subject": "Hello from" + name,
            "text": message})

def send_email(request):
    name = request.POST["name"]
    email = request.POST["email"]
    message = request.POST["message"]
    send_message(name, email, message)
    redirect('/')