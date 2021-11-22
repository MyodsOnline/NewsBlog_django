import datetime
from django.urls import reverse
from django.db import models


class Email(models.Model):
    number = models.PositiveIntegerField(db_index=True, unique=True, verbose_name='Email number')
    date = models.DateField(default=datetime.date.today, verbose_name='Date')
    time = models.TimeField(verbose_name='Time')
    text = models.CharField(max_length=100, blank=True, null=True, verbose_name='Text')
    file = models.FileField(upload_to='docs/%Y/', blank=True, verbose_name='File')
    author = models.CharField(max_length=100, verbose_name='Author')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Created_at')
    is_ok = models.BooleanField(default=False, verbose_name='Is_ok?')

    def __str__(self):
        return f'{self.number}'

    def get_absolute_url(self):
        return reverse('current', kwargs={'email_id': self.pk})

    class Meta:
        verbose_name = 'email'
        verbose_name_plural = 'emails'
        ordering = ['-number']


