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


class Contact(models.Model):
    time = models.CharField(max_length=20, verbose_name='Время работы от и до')
    address = models.CharField(max_length=120, verbose_name='Адрес №1')
    address = models.CharField(
        verbose_name='Адрес №1', 
        max_length=120, 
        null=True, 
        blank=True
    )
    map = models.TextField(verbose_name="Карта")
    phone = models.CharField(max_length=17, verbose_name='Номер телефона №1')
    phone2 = models.CharField(
        verbose_name='Номер телефона №2',
        null=True, blank=True, 
        max_length=17
    ) 
    tg = models.CharField(max_length=50, verbose_name='Телеграм')

    def __str__(self):
        return 'Страница Контакты'

    class Meta:
        verbose_name_plural = "Блок Контакты"
        verbose_name = "контакт"


class ContactForm(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Сообщение обратной связи"
        verbose_name = "cообщение обратной связи"
        ordering = ['-id']
 