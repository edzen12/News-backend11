from django.contrib import admin
from news.models import (Article, Category, About, Comment,
                          Contact, ContactForm)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'created_at']
    search_fields = ('full_name', 'email')
    readonly_fields = ('created_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    search_fields = ('text', 'article__title')
    list_filter = ('created_at',)

admin.site.register(Article)
admin.site.register(About)
admin.site.register(Contact)
