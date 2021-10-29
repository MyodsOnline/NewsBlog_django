from django.shortcuts import render
from django.http import HttpResponse

from .models import News, Category


def index(request):
    orders = News.objects.all()
    context = {
        'title': 'Order_list',
        'content': 'Orders_list',
        'orders': orders,
    }
    return render(request, 'latest_news/index.html', context)


def sender(request):
    context = {
        'sender_title': 'Sender_title',
        'sender_content': 'Email_sender',
        'sender_body': 'sender_body',
    }
    return render(request, 'email_sender/send.html', context)
