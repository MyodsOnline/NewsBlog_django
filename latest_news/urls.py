from django.urls import path

from latest_news.views import index, get_category, get_order

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('order/<int:order_id>/', get_order, name='order'),
]

