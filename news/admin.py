from django.contrib import admin
from news.models import (Article, Category, About,
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

admin.site.register(Article)
admin.site.register(About)
admin.site.register(Contact)
