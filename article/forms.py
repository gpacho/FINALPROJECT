from django.forms import ModelForm
from django import forms
from .models import Article, Comment


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_body',)
        widgets = {
            'comment_body': forms.Textarea(attrs={'class': 'form-control'}),
        }