from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse 
from django.http import HttpResponseNotFound

from .models import Guitar_post
from .models import Youtube_news
from .models import Category_articles
from .templatetags.worldTag import menu

from .forms import Search_form


def home(request):
    post = Guitar_post.objects.all()
    context = {
            'post': post,
            'title': 'Домашняя страница',
            'selected': menu[0]['title']
            }
    return render(request, 'guitar_world/home.html', context=context)

# Отображает категории
def show_category(request, cat_slug):
    cats = Category_articles.objects.all()
    post = Guitar_post.objects.filter(type__slug=cat_slug)
    print(cat_slug)
    context = {
            'post': post,
            'cats': cats,
            'title': 'Домашняя страница',
            'selected': cat_slug
            }
    print(context['selected'])
 
    return render(request, 'guitar_world/articles.html', context=context)

# Читает статью
def read_article(request, read_slug):
    post = get_object_or_404(Guitar_post, slug=read_slug)
    context = {
        'post': post,
        'title': 'Статья',
        'selected': menu[0]['title']
    }
    return render(request, 'guitar_world/read_article.html', context=context)

def search_articles(request):
    form = Search_form()
    context = {
        'title': 'Результат поиска',
        'form': form
    }
    return render(request, 'guitar_world/search.html', context=context)

def articles(request):
    form = Search_form()
    post = Guitar_post.objects.all()
    cats = Category_articles.objects.all()
    check = 'Статьи'
    context = {
            'form': form,
            'post': post,
            'cats': cats,
            'check': check,
            'title': 'Статьи',
            'selected': menu[1]['title']
               }
    return render(request, 'guitar_world/articles.html', context=context)

def add_article(request):
    context = {
            'title': 'Добавить статью',
            'selected': menu[2]['title']
            }
    return render(request, 'guitar_world/add_article.html', context=context)

def guitar_music_news(request):
    post = Youtube_news.objects.all()
    context = {
            'post': post,
            'title': 'Новости гитарной музыки',
            'selected': menu[3]['title']

            }
    return render(request, 'guitar_world/guitar_music_news.html', context=context)

def registration(request):
    context = {
            'title': 'Регистрация',
            'selected': menu[4]['title']
            }
    return render(request, 'guitar_world/registration.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')

