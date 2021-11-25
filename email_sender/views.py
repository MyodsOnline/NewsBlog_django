from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

from .models import Email
from .forms import EmailForm


def sender(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            email_save = form.save()

            """ Sending email with attachment """
            email_number = request.POST.get('number', '')
            email_date = request.POST.get('date', '')
            email_time = request.POST.get('time', '')
            email_text = request.POST.get('text', '')
            email_author = request.POST.get('author', '')
            email_title = f'Email from SO North-West #{email_number}'

            html_content = render_to_string('email_sender/email_tmpl.html', {
                'title': email_title,
                'date_time': f'Moscow time: {email_time}  /  {email_date}',
                'email_number': f'Message # {email_number}',
                'email_text': email_text,
                'email_author': email_author,
            })
            txt_content = strip_tags(html_content)

            email = EmailMultiAlternatives(
                email_title,
                txt_content,
                settings.EMAIL_HOST_USER,
                ['diver.vlz@gmail.com']
            )
            email.attach_alternative(html_content, 'text/html')

            if request.FILES:
                email_file = request.FILES['file']
                email.attach(email_file.name, email_file.read(), email_file.content_type)

            email.send()

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
