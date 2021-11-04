from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class News(models.Model):
    number = models.PositiveIntegerField(db_index=True, unique=True, blank=True)
    title = models.CharField(max_length=100, verbose_name='Заголовок', db_index=True)
    content = models.TextField(verbose_name='Контент')
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    file = models.FileField(upload_to='docs/%Y/', verbose_name='Файл', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    is_starred = models.BooleanField(default=False, blank=True, verbose_name='Избранное')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Категория')

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('order', kwargs={'order_id': self.pk})

    class Meta:
        verbose_name = 'Распрояжение'
        verbose_name_plural = 'Распрояжения'
        ordering = ['-created_at']


class Category(models.Model):
    cat_title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['pk']

    def __str__(self):
        return f'{self.cat_title}'
