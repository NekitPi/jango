from django.shortcuts import render, redirect
from .models import Book, Genre, Publisher, Tag, Comment
from django.http import HttpResponse
from .forms import BookForm
from django.utils.datastructures import MultiValueDictKeyError

def books(request):
    books = Book.objects.all()
    genres = Genre.objects.all()
    publishers = Genre.objects.all()
    return render(request, "index.html", context={"books": books,
                                                  "genres": genres,
                                                  "publishers": publishers})
def get_book(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return HttpResponse(f"<h1> Книги с таким айди: {id} не существует </h1>")

    return render(request, "detail.html", context={"book": book})

def get_genre_books(request, title):
    try:
        genre = Genre.objects.get(title=title)
    except Genre.DoesNotExist:
        return HttpResponse(f"<h1> Жанра с таким названием {title} не существует </h1>")

    return render(request, "genre.html", context={"genre": genre})

def get_tag_books(request, title):
    try:
        tag = Tag.objects.get(title=title)
    except Tag.DoesNotExist:
        return HttpResponse(f"<h1> Тэга с таким название {title} не существует")
    tag_books = tag.books.all()
    return render(request, "tag_detail.html", context={"tag_books": tag_books})

def add_book(request):
    if request.user.is_authenticated:

        if request.method == "GET":
            form = BookForm()
            return render(request, "add_book.html", context={"form": form})
        elif request.method == "POST":
            publisher_id = request.POST['publisher']
            genre_id = request.POST['genre']


            publisher = None
            genre = None
            image = request.FILES.get('image', "default.jpg")

            if publisher_id != '':
                publisher = Publisher.objects.get(id=publisher_id)

            if genre_id != '':
                genre = Genre.objects.get(id=genre_id)

            book = Book.objects.create(title = request.POST['title'],
                                author = request.POST['author'],
                                year=request.POST['year'],
                                raiting=request.POST['raiting'],
                                publisher=publisher,
                                genre=genre,
                                image=image,
                                user = request.user)
            tags = request.POST.getlist('tags')
            book.tags.set(tags)
            book.save()

            return redirect("books")
    else:
        return HttpResponse("<h1>У вас нет прав на это действие!</h1>")

def search_book(request):
    title = request.GET['title']
    genre = request.GET['genre']

    books = Book.objects.all()
    if title != '':
        print("Получил и фильтрую по названию")
        books = books.filter(title__contains=title)
    if genre != '':
        print("Получил и фильтрую по жанру")
        books = books.filter(genre__title__contains = genre)
    return render(request, 'search_book.html', context={"books": books})

def delete_book(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return HttpResponse(f"<h1> Книги с таким айди: {id} не существует </h1>")
    if request.user.username != book.user.username:
        return HttpResponse("<h1> У Вас нет прав на обновление книги! </h1>")
    else:
        book.delete()
        return redirect('books')

def update_book(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return HttpResponse(f"<h1>Книги с таким айди: {id} не существует!</h1>")

    if request.user.username != book.user.username:
        return HttpResponse("<h1> У Вас нет прав на обновление книги! </h1>")

    else:
        if request.method == "GET":
            form = BookForm(instance=book)

            return render(request, "update_book.html", context={"form": form,
                                                                "book": book})
        else:
            publisher_id = request.POST['publisher']
            genre_id = request.POST['genre']

            publisher = None
            genre = None
            image = request.FILES.get('image', "default.jpg")

            if publisher_id != '':
                publisher = Publisher.objects.get(id=publisher_id)

            if genre_id != '':
                genre = Genre.objects.get(id=genre_id)

            book.title = request.POST['title']
            book.author = request.POST['author']
            book.year = request.POST['year']
            book.raiting = request.POST['raiting']
            book.publisher = publisher
            book.genre = genre
            book.image = image
            tags = request.POST.getlist('tags')
            book.tags.set(tags)

            book.save()

            return redirect (get_book, id=book.id)

def add_comment(request, id):
    if request.user.is_authenticated:
        print(request.POST)
        raiting = 5
        try:
            book=Book.objects.get(id=id)
        except Book.DoesNotExist:
            return HttpResponse ("<h1> Такой книги не существует </h1>")
        try:
            Comment.objects.create(content = request.POST['comment'],
                                   raiting = raiting,
                                   user = request.user,
                                   book = book)
        except MultiValueDictKeyError:
            return HttpResponse("<h1>404</h1>")
        return redirect("get_book", id=id)
    else:
        return HttpResponse("<h1> Вы не авторизованы в системе! </h1>")

