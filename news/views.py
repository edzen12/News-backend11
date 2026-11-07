from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from news.models import Article, Category, About, Contact, ContactForm


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

@require_http_methods(['GET', 'POST'])
def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        if full_name and email and message:
            ContactForm.objects.create(
                full_name=full_name,
                email=email,
                message=message
            )
            return redirect('contact_success')

    categories = Category.objects.all()
    contact = Contact.objects.latest('-id')
    context = { 
        'categories':categories,
        'contact':contact,
    }
    return render(request, 'pages/contact.html', context)

def contact_success(request):
    return render(request, 'pages/contact_success.html')


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