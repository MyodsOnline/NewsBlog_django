from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import UpdateView
from django.core.paginator import Paginator

from .models import News, Category
from .forms import OrderForm


def index(request):
    orders = News.objects.all()
    paginator = Paginator(orders, 5)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    categories = Category.objects.all()
    context = {
        'title': 'Order_list',
        'content': 'Orders_list',
        'orders': orders,
        'categories': categories,
        'page_obj': page_objects,
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


def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():

            order = form.save()
            return redirect(index)
    else:
        form = OrderForm()
    categories = Category.objects.all()
    return render(request, 'latest_news/add_order.html', {
        'content': 'Add_order',
        'categories': categories,
        'form': form,
    })


class OrderUpdateView(UpdateView):
    model = News
    template_name = 'latest_news/get_order.html'
    fields = ['number', 'title', 'is_published', 'is_starred']
