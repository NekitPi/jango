from django.core.management.base import BaseCommand
import requests
from books.models import Publisher, Book
import random,django


class Command(BaseCommand):
    help = 'Загрузка книг из другого источника'

    def handle(self, *args, **options):
        print("команда запустилась")
        url = "http://gen.lib.rus.ec/json.php?fields=Title,Author,Year,publisher&ids=1,2,3,4,5,6,7"
        response = (requests.get(url))

        languages = ['ru', 'en', 'fr']

        for book in response.json():
            # print(book['title'])
            # print(book['author'])
            # print(book['year'])
            # print(book['publisher'])
            # print(random.choice(languages))
            language = random.choice(languages)
            raiting = random.choice(["1","2","3","4","5","6","7","8","9","10"])

            if not Publisher.objects.filter(title =book['publisher']).last():
                publisher = Publisher.objects.filter(title=book['publisher'],
                                         language=language)
            else:
                publisher = Publisher.objects.filter(title =book['publisher']).last()
            print(publisher)
            try:
                if not Book.objects.filter(title=book['title']).last():
                    Book.objects.create(title = book['title'],
                                        author = book['author'],
                                        year = book['year'],
                                        raiting = raiting,
                                        publisher=publisher)
            except django.db.utils.IntegrityError:
                Book.objects.create(title=book['title'],
                                    author=book['author'],
                                    year=book['year'],
                                    raiting = raiting)