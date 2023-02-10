from django.urls import path

from guitarworld.views import Home
from guitarworld.views import Articles
from guitarworld.views import add_article
from guitarworld.views import GuitarMusicNews
from guitarworld.views import registration
from guitarworld.views import ReadArticle
from guitarworld.views import ShowCategory
from guitarworld.views import search_articles


urlpatterns = [
        path('', Home.as_view(), name='home'),
        path('articles/', Articles.as_view(), name='articles'),
        path('add_article/', add_article, name='add_article'),
        path('guitar_music_news/', GuitarMusicNews.as_view(), name='guitar_music_news'),
        path('registration/', registration, name='registration'),
        path('search/', search_articles, name='search_articles'),
        
        # Читать статью
        path('read/<slug:read_slug>/', ReadArticle.as_view(), name='read_article'),
        # Отобразить категорию
        path('category/<slug:type_slug>/', ShowCategory.as_view(), name='show_category'),
        ]
