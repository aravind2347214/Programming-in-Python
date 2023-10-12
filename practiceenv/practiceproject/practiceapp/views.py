from django.shortcuts import render
from django.http import HttpRequest

def firstview(req):
    return(render(req,"new/home.html"))

# Create your views here.
