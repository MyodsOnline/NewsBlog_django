from django.shortcuts import render
from django.http import HttpResponse

from .models import News, Category


def index(request):
    orders = News.objects.all()
    context = {
        'title': 'Order list',
        'content': 'Order list',
        'orders': orders,
    }
    return render(request, 'latest_news/index.html', context)


def sender(request):
    context = {
        'sender_title': 'sender_title',
        'sender_content': 'sender_content',
        'sender_body': 'sender_body',
    }
    return render(request, 'email_sender/send.html', context)
