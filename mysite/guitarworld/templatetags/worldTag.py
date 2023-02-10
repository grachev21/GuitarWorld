from django import template
from guitarworld.models import Category_articles

menu = [
        {'title': 'GuitarWorld', 'url_name': 'home'}, 
        {'title': 'Статьи', 'url_name': 'articles'},
        {'title': 'Добавить статью', 'url_name': 'add_article'},
        {'title': 'Новости гитарной музыки', 'url_name': 'guitar_music_news'},
        {'title': 'Регистрация', 'url_name': 'registration'}
    ]
register = template.Library()

@register.inclusion_tag('tag_templates/header_menu.html')
def header_menu(selected):
    return {'menu': menu, 'selected': selected}
    
    

@register.inclusion_tag('tag_templates/menu_categories.html')
def menu_categories(selected, check):
    cats = Category_articles.objects.all() 
    return {'cats': cats, 'selected': selected, 'check': check}

