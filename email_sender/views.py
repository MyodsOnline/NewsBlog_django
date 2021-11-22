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
    next_number = int(str(Email.objects.latest('number'))) + 2
    context = {
        'sender_title': 'ex.FinFax',
        'sender_content': 'Email_sender',
        'email': email,
        'form': form,
        'next': next_number,
    }
    return render(request, 'email_sender/send.html', context)


def current(request, email_id):
    email = get_object_or_404(Email, pk=email_id)
    context = {
        'email': email,
        'title': 'Current: ' + str(email.number)
    }
    return render(request, 'email_sender/current.html', context)
