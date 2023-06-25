from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserForm
from django.contrib.auth.models import User

def register_user(request):
    print("данные, которые я отправляю на сервер")
    if request.method == "GET":
        print(request.POST)
        form = UserForm()
        return render(request, "register.html", context={"form": form})
    else:
        print(request.POST)
        form = UserForm()

        user = User.objects.create_user(username = request.POST['username'],
                                        email = request.POST['email'])

        user.set_password(request.POST['password'])
        user.save()
        return redirect('books')
