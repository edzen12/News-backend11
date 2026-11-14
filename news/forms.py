from django import forms 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from news.models import Comment

class RegistrationForm(forms.Form):
    email = forms.EmailField(
        max_length=150,
        widget=forms.EmailInput(attrs={
            'class':'form-control', 
            'placeholder':'Введите почту'}
        ) 
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'Введите пароль',
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'Повторно введите пароль',
        })
    )

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        User = get_user_model()
        if User.objects.filter(username__iexact=email).exists():
            raise forms.ValidationError(
                'Пользователь с таким email уже существует'
            )
        return email 

    def clean(self):
        data = super().clean()
        password1 = data.get('password1')
        password2 = data.get('password2')
        if password1 and password2:
            if password1 != password2:
                self.add_error(
                    'password2', 'Пароли не совпадают'
                )
        if password1:
            User = get_user_model()
            email = data.get('email', '')
            user = User(username=email, email=email)
            try:
                validate_password(password1, user)
            except ValidationError as error:
                self.add_error('password1', error)
        return data


class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email',max_length=150,
        widget=forms.EmailInput(attrs={
            'class':'form-control', 
            'placeholder':'Введите почту'
        }) 
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({
            'class':'form-control', 
            'placeholder':'Пароль'
        })

    def clean_username(self):
        return self.cleaned_data['username'].lower()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
            'class': 'form-control', 
            'rows': 4,
            'placeholder':'Напишите комментарии'
            })
        }