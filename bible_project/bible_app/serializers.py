from rest_framework import serializers
from .models import Book, Chapter, Verse

class VerseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verse
        fields = ['number', 'text']


class ChapterSerializer(serializers.ModelSerializer):
    verses = VerseSerializer(many=True, read_only=True)
    book = serializers.SerializerMethodField()

    class Meta:
        model = Chapter
        fields = ['number', 'verses', 'book']

    def get_book(self, obj):
        return BookSerializer(obj.book).data
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['verses'] = sorted(rep['verses'], key=lambda x: x['number'])
        return rep

class BookSerializer(serializers.ModelSerializer):
    # chapters = ChapterSerializer(many=True)
    number_of_chapters = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['name', 'number_of_chapters']

    def get_number_of_chapters(self, obj):
        return Chapter.objects.filter(book_id=obj).count()