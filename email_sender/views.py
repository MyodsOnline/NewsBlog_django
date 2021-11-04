from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Email


def sender(request):
    email = Email.objects.all()
    context = {
        'sender_content': 'Email_sender',
        'email': email,
    }
    return render(request, 'email_sender/send.html', context)


def current(request, email_id):
    email = get_object_or_404(Email, pk=email_id)
    context = {
        'email': email,
        'title': 'Current: ' + str(email.number)
    }
    return render(request, 'email_sender/current.html', context)
