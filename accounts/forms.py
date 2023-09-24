import allauth.account.forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.core.mail import send_mail

from blog.models import Author


# Форма регистрации
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


# Привязка группы "authors" по умолчанию к зарегистрированному пользователю
class CustomSignupForm(SignupForm):
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    def save(self, request):
        user = super().save(request)
        authors = Group.objects.get(name="authors")
        send_mail(
            subject='Добро пожаловать в наш интернет-магазин!',
            message=f'{user.username}, вы успешно зарегистрировались!',
            from_email=None,  # будет использовано значение DEFAULT_FROM_EMAIL
            recipient_list=[user.email],
        )
        if not request.user.groups.filter(name='authors').exists():
            authors.user_set.add(user)
            user.groups.add(authors)
        return user

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
        )
