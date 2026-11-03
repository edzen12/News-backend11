from django.shortcuts import render, get_object_or_404
from news.models import Article, Category


def homepage(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    context = {
        'articles':articles,
        'categories':categories,
    }
    return render(request, 'index.html', context) 


def category_news(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(category=category)
    categories = Category.objects.all()
    context = {
        'articles':articles,
        'categories':categories,
        'current_category':category,
    }
    return render(request, 'category.html', context) 