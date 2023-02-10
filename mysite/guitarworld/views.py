from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.views.generic import ListView
from django.views.generic import DetailView

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

# # Читает статью
# def read_article(request, read_slug):
#     post = get_object_or_404(Guitar_post, slug=read_slug)
#     context = {
#         'post': post,
#         'title': 'Статья',
#         'selected': menu[0]['title']
#     }
#     return render(request, 'guitar_world/read_article.html', context=context)

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
    return render(request, 'guitar_world/search.html', context=context)


def articles(request):

    post = Guitar_post.objects.all()
    cats = Category_articles.objects.all()
    check = 'Статьи'

    context = {'post': post,
               'cats': cats,
               'check': check,
               'title': 'Статьи',
               'selected': menu[1]['title']}

    return render(request, 'guitar_world/articles.html', context=context)

def add_article(request):
    if request.method == 'POST':
        form = Add_article(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Add_article()
            
    context = {
            'form': form,
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

