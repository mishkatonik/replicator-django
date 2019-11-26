import requests
import json
from django.http import HttpResponse
from django.shortcuts import render

def replicator(request):
    replicator_content = open('templates/the-replicator.html').read()
    context = {
        'title': 'Welcome to the Replicator!',
        'content': replicator_content,
    }
    return render(request, 'base.html', context)


def about(request):
    about_content = open('templates/about.html').read()
    context = {
        'title': 'About - The Food of Star Trek',
        'content': about_content,
    }
    return render(request, 'base.html', context)


def meet_the_chef(request):
    chef_content = open('templates/meet-the-chef.html').read()
    context = {
        'title': 'Meet the Chef',
        'content': chef_content,
    }
    return render(request, 'base.html', context)

def contact(request):
    contact_content = open('templates/contact.html').read()
    context = {
        'title': 'Contact Me',
        'content': contact_content,
    }
    return render(request, 'base.html', context)

# MailGun example email method -----------------------------------------------------------------
def send_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxff6f95855b4243fea79d198ec524098d.mailgun.org/messages",
        auth=("api", "010b9271dac02ac74fec58f880dca8c5-09001d55-e01ed707"),
        data={"from": "Mailgun Sandbox <postmaster@sandboxff6f95855b4243fea79d198ec524098d.mailgun.org>",
            "to": "Mish Mercer <mishell.mercer@gmail.com>",
            "subject": "Hello Mish Mercer",
            "text": "Congratulations Mish Mercer, you just sent an email with Mailgun!  You are truly awesome!"})