# Generated by Django 3.2.5 on 2021-10-31 05:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(db_index=True, unique=True, verbose_name='Email number')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('time', models.TimeField(verbose_name='Time')),
                ('text', models.CharField(blank=True, max_length=100, null=True, verbose_name='Text')),
                ('file', models.FileField(blank=True, upload_to='docs/%Y/', verbose_name='File')),
                ('author', models.CharField(max_length=100, verbose_name='Author')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('is_ok', models.BooleanField(default=False, verbose_name='Is_ok?')),
            ],
            options={
                'verbose_name': 'email',
                'verbose_name_plural': 'emails',
                'ordering': ['-number'],
            },
        ),
    ]
