from django.contrib import admin
from news.models import Article, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

admin.site.register(Article)
admin.site.register(Category, CategoryAdmin)