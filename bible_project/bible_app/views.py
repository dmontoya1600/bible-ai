from rest_framework import viewsets
from rest_framework.response import Response
from .models import Book, Chapter, Verse
from .serializers import BookSerializer, VerseSerializer, ChapterSerializer
from django.shortcuts import get_object_or_404

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'name'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, name=self.kwargs["pk"])
        return obj


class VerseViewSet(viewsets.ModelViewSet):
    serializer_class = VerseSerializer

    def get_queryset(self):
        book = get_object_or_404(Book, name=self.kwargs["book_name"])
        chapter = book.get_chapter(chapter_number=self.kwargs["chapter_number"])
        return Verse.objects.filter(chapter=chapter).order_by('number')

class ChapterViewSet(viewsets.ModelViewSet):
    serializer_class = ChapterSerializer
    lookup_field = 'number'

    def get_queryset(self):
        book_name = self.kwargs['book_name']
        return Chapter.objects.filter(book__name=book_name)

    def get_object(self):
        queryset = self.get_queryset()
        filter_kwargs = {self.lookup_field: self.kwargs['chapter_number']}
        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj
