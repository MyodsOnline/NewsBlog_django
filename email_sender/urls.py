from django.urls import path, include

from latest_news.views import sender

urlpatterns = [
    path('', sender),
]
