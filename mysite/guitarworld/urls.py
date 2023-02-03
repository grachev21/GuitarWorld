from django.urls import path

from guitarworld.views import home
from guitarworld.views import articles
from guitarworld.views import add_article
from guitarworld.views import guitar_music_news
from guitarworld.views import registration
from guitarworld.views import read_article
from guitarworld.views import show_category
from guitarworld.views import search_articles


urlpatterns = [
        path('', home, name='home'),
        path('articles/', articles, name='articles'),
        path('add_article/', add_article, name='add_article'),
        path('guitar_music_news/', guitar_music_news, name='guitar_music_news'),
        path('registration/', registration, name='registration'),
        path('search/', search_articles, name='search_articles'),
        
        # Читать статью
        path('read/<slug:read_slug>/', read_article, name='read_article'),
        # Отобразить категорию
        path('category/<slug:cat_slug>/', show_category, name='show_category'),
        ]
