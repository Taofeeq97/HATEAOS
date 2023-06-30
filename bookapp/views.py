from django.shortcuts import render
from rest_framework import generics
from .serializer import BookSerializer
from .models import Book
from drf_spectacular.openapi import AutoSchema
from .activitymixin import ActivityLogMixin
from .index import BookIndex
from algoliasearch_django import raw_search


class BookListApiView(ActivityLogMixin, generics.ListAPIView):
    schema = AutoSchema()
    queryset = Book.objects.filter(is_active=True)
    serializer_class = BookSerializer    

    def get_log_message(self, request) -> str:
        return f"{request.user} is viewing the books list"

def print_request_attributes(request):
    attributes = dir(request)
    for attribute in attributes:
        print(attribute)

    

class BookDetailApiView(ActivityLogMixin, generics.RetrieveAPIView):
    schema = AutoSchema()
    queryset = Book.objects.all()
    serializer_class =BookSerializer
    lookup_field = 'pk'

    
    def get_log_message(self, request) -> str:
        return f"{request.user} is viewing the books detail"
    


class BookUpdateApiView(ActivityLogMixin, generics.UpdateAPIView):
    schema = AutoSchema()
    queryset =Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

    def get_log_message(self, request) -> str:
        return f"{request.user} update a book instance"


class BookDeleteApiView(generics.DestroyAPIView):
    schema= AutoSchema()
    queryset =Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

    def get_log_message(self, request) -> str:
        return f"{request.user} is deleted the book"