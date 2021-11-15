from django.http import HttpResponseRedirect as redirect, HttpResponse as response
from django.shortcuts import render
from FirstApp.models import *


# My views are here.


def index(request):
    try:
        perms = 0
        if request.session['user_id']:
            print(request.session['user_id'])
            user = User.objects.get(id=request.session['user_id'])
            name = [user.name, "", ""]
            perms = user.permissions
            print(request.session['user_id'])
        else:
            name = ["рованнй поьовтль", "", ""]
    except:
        name = ["незарегистрированный пользователь", "", ""]
        perms = 0
    host = request.get_host() # нужен для сессии
    data2send = {"name": name, "host": host, "perms": perms}
    return render(request, "index.html", data2send)


def register(request):
    if request.method == "POST":
        user = User()
        try:
            user.name = request.POST.get("name")
            user.nick = request.POST.get("nick")
            user.password = request.POST.get("password")
        except:
            return response("ошибка в ПОСТ")
        try:
            user.save()
            user = User.objects.get(nick=request.POST.get("nick"),
                                    password=request.POST.get("password"))
            request.session['user_id'] = user.id
            return redirect('/index/')
        except:
            return response("Такой логин уже есть, о восстановлении пароля просите админа.")


def login(request):
    if request.method == "POST":
        try:
            user = User.objects.get(nick=request.POST.get("nick"),
                                    password=request.POST.get("password"))
            print(user)
            request.session['user_id'] = user.id
            return redirect('/index/')
        except:
            return redirect('/error/')


def error(request):
    return response("""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Ошибка</title>
</head>
<body>
  <h1>ОШИБКА: логин/пароль неверны.</h1>
  <form action="/index/"><input type="submit" value="Вернуться на главную!"></form>
</body>
</html>""")


def clear_session(request):
    try:
        del request.session['user_id']
        return redirect('/index/')
    except:
        return response("ошибка при выходе из аккаунта, сообщите админу")