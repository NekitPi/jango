from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserForm, LoginUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
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
            return HttpResponse("<h1> Логин и пароль верный, вы можете войти! </h1>")
        else:
            return HttpResponse("<h1> Проверьте правильность пароля </h1>")
        print(user)
        form = LoginUserForm()

        return render(request, "login_user.html", context={"form": form})
