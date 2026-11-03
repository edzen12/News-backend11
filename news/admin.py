from django.contrib import admin
from news.models import Article, Category, About


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

admin.site.register(Category, CategoryAdmin)

admin.site.register(Article)
admin.site.register(About)