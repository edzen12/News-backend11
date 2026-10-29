from django.shortcuts import render
from news.models import Article, Category


def homepage(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    context = {
        'articles':articles,
        'categories':categories,
    }
    return render(request, 'index.html', context) 