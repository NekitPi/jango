from django.urls import path, include
from books.views import books, get_book, get_genre_books, get_tag_books, add_book, search_book, delete_book, update_book, add_comment

urlpatterns = [
    path('get_books/', books, name='books'),

    path('get_books/<int:id>/', get_book, name="get_book"),
    path('get_genre/<str:title>/', get_genre_books, name="get_genre"),
    path('add_book/', add_book, name="add_book"),
    path('update_book/<int:id>/', update_book, name="update_book_by_id"),
    path('search_book/', search_book, name="search_book"),
    path('delete_book/<int:id>/', delete_book, name="delete_book"),
    path('add_comment/<int:id>/', add_comment, name="add_comment"),

    path('get_tag/<str:title>/', get_tag_books, name="get_tag_books"),
]