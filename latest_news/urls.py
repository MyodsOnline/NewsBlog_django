from django.urls import path

from latest_news.views import index, get_category

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', get_category),
]

