from django.shortcuts import render, get_object_or_404
from news.models import Article, Category, About


def homepage(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    context = {
        'articles':articles,
        'categories':categories,
    }
    return render(request, 'index.html', context) 

def about(request):
    categories = Category.objects.all()
    about = About.objects.latest('id')
    context = { 
        'categories':categories,
        'about':about,
    }
    return render(request, 'pages/about.html', context)

def contact(request):
    categories = Category.objects.all()
    context = { 
        'categories':categories,
    }
    return render(request, 'pages/contact.html', context)


def category_news(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(category=category)
    categories = Category.objects.all()
    context = {
        'articles':articles,
        'categories':categories,
        'current_category':category,
    }
    return render(request, 'pages/category.html', context) 