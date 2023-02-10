from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView

from .models import Guitar_post
from .models import Youtube_news
from .models import Category_articles
from .templatetags.worldTag import menu

from .forms import Search_form
from .forms import Add_article


class Home(ListView):
    model = Guitar_post
    template_name = 'guitar_world/home.html'
    context_object_name = 'post'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected'] = menu[0]['title']
        context['title'] = 'GuitarWorld'
        return context

class ShowCategory(ListView):
    model = Guitar_post
    template_name = 'guitar_world/articles.html'
    context_object_name = 'post'
    allow_empty = False

    def get_queryset(self):
        return Guitar_post.objects.filter(type__slug=self.kwargs['type_slug'])
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['post'][0].type) 
        context['selected'] = context['post'][0].type_id
        print(str(context['post'][0].type_id))
        return context


class ReadArticle(DetailView):
    model = Guitar_post
    template_name = 'guitar_world/read_article.html'
    slug_url_kwarg = 'read_slug'    
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        return context

# Заморозил!
def search_articles(request):
    post = None
    id_value = []
    if request.method=='POST':
        form = Search_form(request.POST) 
        if form.is_valid():
            search_result = form.cleaned_data
            result = search_result['value']
            print('До поиск - ', result)

            post =  Guitar_post.objects.get(title=result)
            print(post)
    else:
        form = Search_form()

    context = {
        'post':post,
        'id_value': id_value,
        'title': 'Результат поиска',
        'form': form
    }
    return render(request, 'guitar_world/articles.html', context=context)

class Articles(ListView):
    model = Guitar_post
    template_name = 'guitar_world/articles.html'
    context_object_name = 'post'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['check'] = 'Статьи'
        context['title'] = 'Статьи'
        context['selected'] = menu[1]['title']
        return context


class AddArticle(CreateView):
    form_class = Add_article
    template_name = 'guitar_world/add_article.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить статью'
        context['selected'] = menu[2]['title']
        return context


class GuitarMusicNews(ListView):
    model = Youtube_news
    template_name = 'guitar_world/guitar_music_news.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости гитарной музыки'
        context['selected'] = menu[3]['title']
        return context

class Registration(ListView):
    model = Guitar_post
    template_name = 'guitar_world/registration.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        context['selected'] = menu[4]['title']
        return context

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')

