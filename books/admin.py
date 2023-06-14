from django.contrib import admin
from .models import Book, Genre, Movie, Category, Tag, Publisher

class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "raiting", "year", "publisher", "genre", "get_tags", "created_at")

    def get_tags(self, obj):
        tags = obj.tags.all()
        return "\n".join([str(t) for t in tags])
admin.site.register(Book, BookAdmin)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Publisher)