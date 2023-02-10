from django.db import models
from django.urls import reverse


class Category_articles(models.Model):
    type = models.CharField(max_length=100, db_index=True, verbose_name='Тип')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('show_category', kwargs={'type_slug': self.slug})

    class Meta:
        verbose_name = 'Тип статьи'
        verbose_name_plural = 'Тип статей'
        ordering = ['type',]

class Guitar_post(models.Model):
    title = models.CharField(max_length=244, verbose_name='Заголовок') 
    content = models.TextField(blank=True, verbose_name='Текст')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    type = models.ForeignKey(Category_articles, on_delete=models.PROTECT, verbose_name='Тип статьи')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('read_article', kwargs={'read_slug': self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['time_create', 'title']

class Youtube_news(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(blank=True, verbose_name='Описание')
    photo_link =  models.URLField(verbose_name='Ссылка на фото')
    link = models.URLField(verbose_name='Ссылка на видео')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('?', kwargs={'': self.pk})

    class Meta:
        verbose_name = 'Новости YouTube'
        verbose_name_plural = 'Новости YouTube'
        ordering = ['title']
