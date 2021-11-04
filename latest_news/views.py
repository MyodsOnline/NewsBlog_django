from django.shortcuts import render
from django.shortcuts import get_object_or_404

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


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'latest_news/category.html', {
        'news': news,
        'categories': categories,
        'category': category,
        'content': 'Orders_list/' + category.cat_title,
    })


def get_order(request, order_id):
    order = get_object_or_404(News, pk=order_id)
    return render(request, 'latest_news/order.html', {
        'order': order,
        'title': 'Orders_list/' + str(order.number),
    })
