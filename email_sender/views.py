from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.core.mail import send_mail, EmailMessage

from .models import Email
from .forms import EmailForm
from NewsBlog import settings


def sender(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            email_save = form.save()

            email_text = request.POST.get('text')
            email_author = request.POST.get('author')
            email_date = request.POST.get('date')
            email_time = request.POST.get('time')
            email_number = request.POST.get('number')
            email_title = f'Email from SO of North-West #{email_number}'
            content = f'{email_date} {email_time} / {email_number}\n\n' \
                      f'{email_text}\nBest regards, {email_author}.'

            send_mail(email_title,
                      content,
                      settings.EMAIL_HOST_USER,
                      ['diver.vlz@gmail.com'],
                      fail_silently=False,)

            return redirect(sender)
    else:
        form = EmailForm()
    email = Email.objects.all()

    paginator = Paginator(email, 10)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)

    next_number = int(str(Email.objects.latest('number'))) + 2

    context = {
        'sender_title': 'ex.FinFax',
        'sender_content': 'Email_sender',
        'email': email,
        'form': form,
        'next': next_number,
        'page_obj': page_objects,
    }
    return render(request, 'email_sender/send.html', context)


def current(request, email_id):
    email = get_object_or_404(Email, pk=email_id)
    context = {
        'email': email,
        'title': 'Current: ' + str(email.number)
    }
    return render(request, 'email_sender/current.html', context)
