from django.shortcuts import render
from .models import Book, Genre, Publisher, Tag
from django.http import HttpResponse
from .forms import BookForm

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
    form = BookForm()
    return render(request,"add_book.html", context={"form": form})

def create_book(request):
    print (request.POST)
    genre = Genre.objects.get(id=requests.POST['genre'])
    Book.objects.create(title = request.POST ['title'],
                        author = requests.POST ['author'],
                        tags = request.POST ['tags'],
                        raiting = requests.POST['raiting'],)
                        # publisher = requests.POST['publisher'],
                        # genre = requests.POST['genre'])
    return HttpResponse("<h1> Получилось! </h1>")