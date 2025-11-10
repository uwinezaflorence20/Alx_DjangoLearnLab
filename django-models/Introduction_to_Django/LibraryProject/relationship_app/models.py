from django.db import models

# Create your models here.

from django.db import models


class Author(models.Model):
    """
    Author model representing book authors.
    Demonstrates the "one" side of a ForeignKey relationship.
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model with a ForeignKey relationship to Author.
    Demonstrates Many-to-One relationship:
    - Each book has one author
    - An author can have multiple books
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Library(models.Model):
    """
    Library model with a ManyToMany relationship to Book.
    Demonstrates Many-to-Many relationship:
    - A library can have multiple books
    - A book can be in multiple libraries
    """
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Librarian(models.Model):
    """
    Librarian model with a OneToOne relationship to Library.
    Demonstrates One-to-One relationship:
    - Each library has exactly one librarian
    - Each librarian manages exactly one library
    """
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name