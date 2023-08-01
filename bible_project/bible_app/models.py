from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_chapter(self, chapter_number):
        return self.chapter_set.get(number=chapter_number)

class Chapter(models.Model):
    number = models.IntegerField()
    book = models.ForeignKey(Book, related_name='chapters', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.name} {self.number}"

class Verse(models.Model):
    number = models.IntegerField()
    chapter = models.ForeignKey(Chapter, related_name='verses', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.chapter.book.name} {self.chapter.number}:{self.number}"
