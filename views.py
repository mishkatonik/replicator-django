import requests
import json
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     # This is similar to ones we have done before. Instead of keeping
#     # the HTML / template in a separate directory, we just reply with
#     # the HTML embedded here.
#     return HttpResponse('''
#         <h1>Welcome to my home page!</h1>
#         <a href="/about-me">About me</a> <br />
#         <a href="/github-api-example">See my GitHub contributions</a> <br />
#     ''')


# def about_me(request):
#     # Django comes with a "shortcut" function called "render", that
#     # lets us read in HTML template files in separate directories to
#     # keep our code better organized.
#     context = {
#         'name': 'Ash Ketchum',
#         'pokemon': 'Pikachu',
#     }
#     return render(request, 'about_me.html', context)


# def github_api_example(request):
#     # We can also combine Django with APIs
#     response = requests.get('https://api.github.com/users/michaelpb/repos')
#     repos = response.json()
#     context = {
#         'github_repos': repos,
#     }
#     return render(request, 'github.html', context)


# --------------------------------------------------------------------------------------

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