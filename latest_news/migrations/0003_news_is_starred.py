# Generated by Django 3.2.8 on 2021-11-04 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latest_news', '0002_alter_news_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='is_starred',
            field=models.BooleanField(blank=True, default=False, verbose_name='Избранное'),
        ),
    ]
