from django.shortcuts import render
from django.http import HttpResponse

from .models import News, Category


def index(request):
    orders = News.objects.all()
    categories = Category.objects.all()
    context = {
        'title': 'Order_list',
        'content': 'Orders_list',
        'orders': orders,
        'categories': categories,
    }
    return render(request, 'latest_news/index.html', context)
