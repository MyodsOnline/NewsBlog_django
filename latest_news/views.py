from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Hello</h1>')

def sender(request):
    return HttpResponse('<h1>Fax Page</h1>')