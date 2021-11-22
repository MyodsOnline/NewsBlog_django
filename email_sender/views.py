from django.shortcuts import render, get_object_or_404, redirect

from .models import Email
from .forms import EmailForm


def sender(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            email_save = form.save()
            return redirect(sender)
    else:
        form = EmailForm()
    email = Email.objects.all()
    context = {
        'sender_content': 'Email_sender',
        'email': email,
        'form': form,
    }
    return render(request, 'email_sender/send.html', context)


def current(request, email_id):
    email = get_object_or_404(Email, pk=email_id)
    context = {
        'email': email,
        'title': 'Current: ' + str(email.number)
    }
    return render(request, 'email_sender/current.html', context)
