from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from news.views import homepage, category_news, about, contact, contact_success


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('category/<int:category_id>/', category_news, name='category_news'), 
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('contact/success/', contact_success, name='contact_success'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)