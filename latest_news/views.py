from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'title': 'title',
        'content': 'content',
        'body': 'body',
    }
    return render(request, 'latest_news/index.html', context)


def sender(request):
    context = {
        'sender_title': 'sender_title',
        'sender_content': 'sender_content',
        'sender_body': 'sender_body',
    }
    return render(request, 'email_sender/send.html', context)
