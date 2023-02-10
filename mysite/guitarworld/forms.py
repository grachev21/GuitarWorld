from django import forms
from django.core.exceptions import ValidationError
from .models import Guitar_post

from .models import Category_articles


class Search_form(forms.Form):
    value = forms.CharField(max_length=255, label='Поиск',
                    widget=forms.TextInput(attrs={'class': 'title-search'}))
    # slug = forms.SlugField(max_length=255, label='Слог')
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    # type = forms.ModelChoiceField(queryset=Category_articles.objects.all(), label='Категория', empty_label='Не выбрана')


class Add_article(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].empty_label = 'Категория не выбрана'
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длинна превышает 200 символов')

        return title

    class Meta:
        model = Guitar_post
        fields = ['title', 'content', 'type', 'slug', 'photo']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'title_article'}),
            'content': forms.Textarea(attrs={'cols': 30, 'rows': 10}),

}
        
