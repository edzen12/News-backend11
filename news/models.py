from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'категория'
        ordering = ['-id']


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to='articles/', null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Посты'
        verbose_name = 'пост'
        ordering = ['-id']


class About(models.Model):
    title1 = models.CharField(max_length=100)
    title2 = models.CharField(
        max_length=100, blank=True, null=True
    )
    desc1 = models.TextField()
    desc2 = models.TextField(blank=True, null=True)
    img1 = models.ImageField(upload_to='about/')
    img2 = models.ImageField(
        upload_to='about/', blank=True, null=True
    )

    class Meta:
        verbose_name_plural = 'Блок: О нас'
        verbose_name = 'о нас'

    def __str__(self):
        return self.title1