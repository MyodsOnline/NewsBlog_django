from django.urls import path

from email_sender.views import sender, current

urlpatterns = [
    path('', sender, name='sender'),
    path('email/<int:email_id>', current, name='current'),
]
