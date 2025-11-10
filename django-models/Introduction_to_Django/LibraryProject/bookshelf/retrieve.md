# Retrieve Operation

## Command
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")
```

## Output
```
Title: 1984, Author: George Orwell, Publication Year: 1949
```

## Description
Successfully retrieved the Book instance and displayed all its attributes.