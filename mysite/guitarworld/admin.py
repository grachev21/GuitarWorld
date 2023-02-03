from django.contrib import admin
from .models import Category_articles
from .models import Guitar_post
from .models import Youtube_news


class Guitar_postAdmin(admin.ModelAdmin):
    list_display = ('id',  'title', 'time_create', 'time_update', 'photo', 'type')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('time_create',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Guitar_post, Guitar_postAdmin)

class Category_articlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')
    list_display_links = ('id', 'type')
    prepopulated_fields = {'slug': ('type',)}

admin.site.register(Category_articles, Category_articlesAdmin)

class Youtube_newsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo_link') 
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')

admin.site.register(Youtube_news, Youtube_newsAdmin)