from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from datetime import datetime

# Create your views here.
def index(request):
    articles = Article.objects.all()
    eachArticle = Article.objects.get(pk=1)
    return render(request, 'articles_index.html', {'articles': articles, 'eachArticle': eachArticle})


def detail(request):
    article = Article.objects.get(pk=1)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            
            return redirect('index')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles_detail.html', {'article': article, 'form': form})


def add_comment(request, pk):
    eachArticle = Article.objects.get(id=pk)

    form = CommentForm(instance=eachArticle)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=eachArticle)
        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['comment_body']
            c = Comment(product=eachArticle, commenter_name=name, comment_body=body, date_added=datetime.now())
            c.save()
            return redirect('index')
        else:
            print('form is invalid')    
    else:
        form = CommentForm()    


    context = {
        'form': form
    }

    return render(request, 'articles_detail.html', context)
