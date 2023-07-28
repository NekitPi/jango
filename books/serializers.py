from rest_framework.serializers import ModelSerializer
from .models import Book, Genre, Publisher
from rest_framework import serializers

class CreateBookSerializer(ModelSerializer):
    tags_ids = serializers.CharField()

    def validate_tags_ids(self, value:str):
        print(value)
        value(split(', '))

        print (value)
        return ("Тэги")

    class Meta:
        model = Book
        fields = ['title', 'author', 'year',  'raiting', 'price', 'genre']

class GenreBookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price', 'count']

class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'title']

class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'title', 'language']
class BookSerializer(ModelSerializer):
    genre_title = serializers.SerializerMethodField()
    publisher_title = serializers.SerializerMethodField()

    tags_titles = serializers.SerializerMethodField()


    def get_tags_titles(self,book):
        tags = []
        for tag in book.tags.all():
            tags.append(tag.title)
        return tags

    def get_publisher_title(self,book):
        if book.publisher is not None:
            return book.publisher.title
        return "Нет издателя"

    def get_genre_title(self, book):
        if book.genre is not None:
            return book.genre.title
        return "Нет жанра"

    class Meta:
        model = Book
        fields = ['id', 'title', 'author',  'genre_title', 'publisher_title', 'tags_titles']