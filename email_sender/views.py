from django.shortcuts import render

from .models import Email


def sender(request):
    context = {
        'email': 'Sender_title',
        'sender_content': 'Email_sender',
        'sender_body': 'sender_body',
    }
    return render(request, 'email_sender/send.html', context)


def current(request):
    email = Email.objects.get(pk=1)
    context = {
        'email': email,
        'title': 'Current email'
    }
    return render(request, 'email_sender/current.html', context)
