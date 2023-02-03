from django import forms
from .models import Guitar_post
from .models import Category_articles


class Search_form(forms.Form):
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    type = forms.ModelChoiceField(queryset=Category_articles.objects.all())