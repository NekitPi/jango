from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserForm, LoginUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

import django

def register_user(request):
    print("данные, которые я отправляю на сервер")
    if request.method == "GET":
        print("GET")
        form = UserForm()
        return render(request, "register.html", context={"form": form})
    else:
        email = request.POST['email']
        if User.objects.filter(email=email).count() !=0:
            return HttpResponse("<h1> Пользователь с таким мылом уже существует </h1>")
        else:
            try:
                user = User.objects.create_user(username=request.POST['username'], email = email)

            except django.db.utils.IntegrityError:
                return HttpResponse("<h1> Пользователь с таким логином существует </h1>")
            user.set_password(request.POST['password'])
            user.save()
            send_mail('Успешная регистрация!',
                      'Вы успешно зарегистрировались!',
                      settings.DEFAULT_FROM_EMAIL,
                      settings.RECIPIENTS_EMAIL)
            return HttpResponse("<h1> Вы успешно зарегались! </h1>")

def login_user(request):
    if request.method == "GET":
        form = LoginUserForm()

        return render (request, "login_user.html", context={"form" : form})

    else:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user = user)
        else:
            return HttpResponse("<h1> Что-то пошло не так </h1>")
        return redirect('books')


def logout_user(request):
    logout(request)
    return redirect('books')