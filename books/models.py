from django.db import models

# Create your models here.
class BookRecommendation(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.CharField(max_length=10)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    google_books_id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title