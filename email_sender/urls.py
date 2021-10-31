from django.urls import path, include

from email_sender.views import sender, current

urlpatterns = [
    path('', sender, name='sender'),
    path('test/', current, name='current'),
]
