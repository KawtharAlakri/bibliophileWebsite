from djongo import models
# Create your models here.

class Book(models.Model):
    name=models.TextField()
    author=models.TextField()
    desc=models.TextField(default="No description provided.")
    pages=models.PositiveIntegerField()
    genre=models.TextField()
    ISBN=models.TextField()
    cover=models.CharField(max_length=100)

class Review(models.Model):
    author=models.CharField(max_length=60)
    title=models.TextField(default="")
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    book_item=models.ForeignKey('Book', on_delete=models.CASCADE)
