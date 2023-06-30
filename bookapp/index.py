from algoliasearch_django.decorators import register
from .models import Book
from algoliasearch_django import AlgoliaIndex


@register(Book)
class BookIndex(AlgoliaIndex):
    model = Book
    fields = ['title', 'description']
    settings = {
        "searchableAttributes": ['title', 'description'],
        "attributesForFaceting": []
    }
